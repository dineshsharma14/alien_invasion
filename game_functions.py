import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event,ai_settings,screen,stats,sb,ship,aliens,
    bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        #ship.rect.centerx += 1
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        filename = 'high_score.txt'
        with open(filename,'w') as fileobject:
            fileobject.write(str(stats.high_score))
            sys.exit()
    elif event.key == pygame.K_p:
        filename = 'high_score.txt'
        ai_settings.initialize_dynamic_settings()
        start_game(ai_settings,screen,stats,sb,ship,aliens,bullets)
        
def fire_bullet(ai_settings,screen,ship,bullets):
    """Fire a bullet if limit not reached yet."""
    #Create new bullet and add it to bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    """Respond to keypresses and mouse events."""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            filename = 'high_score.txt'
            with open(filename,'w') as fileobject:
                fileobject.write(str(stats.high_score))
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,stats,sb,ship,
                aliens,bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,
             aliens,bullets,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,
    bullets,mouse_x,mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()
        start_game(ai_settings,screen,stats,sb,ship,aliens,bullets)

def start_game(ai_settings,screen,stats,sb,ship,aliens,bullets):
    #Hide mouse cursor.
    pygame.mouse.set_visible(False)
    
    #Reset the game statistics.
    stats.reset_stats()
    stats.game_active = True

    #Reset scoreboard images
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()
    
    #Empty the list of aliens and bullets.
    aliens.empty()
    bullets.empty()
    
    #Create new alien fleet and center the ship.
    create_fleet(ai_settings,screen,ship,aliens)
    ship.center_ship()
    
def update_bullets(ai_settings,screen,ship,sb,stats,bullets,aliens):
    """Update position of the bullets and get rid of the old bullets"""
    #update bullet position.
    bullets.update()
    #Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.y <= 0:
            bullets.remove(bullet)
    #print(len(bullets))

    check_bullet_alien_collisions(ai_settings,screen,ship,sb,stats,
        aliens,bullets)

def check_bullet_alien_collisions(ai_settings,screen,ship,sb,stats,
    aliens,bullets):
    """Respond to bullet-alien collisions."""
    # Check for any bullets that have hit aliens.
    # If so,get rid of bullet and alien.
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(sb,stats)
        
    if len(aliens) == 0:
        # Destroy existing bullets,speed up game and create new fleet.
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings,screen,ship,aliens)
        stats.level += 1
        sb.prep_level()
            
def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,
    play_button):
    """Updates images on screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)

    # Drawing the aliens
    #aliens.draw(screen)
    # draw() on a group automatically draws each element of grp at position,
    # defined by its rect
    for alien in aliens:
        alien.blitme()

    # Redraw all bullets behind the ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    #Draw the score information.
    sb.show_score()

    #Draw the play button if the game is inactive. Last so that it comes up
    #on top of the screen.
    if not stats.game_active:
        play_button.draw_button()

    # Make most recently drawn screen visible.
    pygame.display.flip()

def get_number_aliens(ai_settings,alien_width):
    """function to calculate number of aliens fitted on screen"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    alien_numberx = int(available_space_x /(2 * alien_width))
    return alien_numberx

def create_alien(ai_settings,screen,aliens,alien_counter,row_number):
    """Create alien and place it in a row."""
    alien = Alien(screen,ai_settings)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_counter
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
    
def create_fleet(ai_settings,screen,ship,aliens):
    """Creates fleet of aliens."""
    alien = Alien(screen,ai_settings)
    alien_numberx = get_number_aliens(ai_settings,alien.rect.width)
    number_rows = int(get_number_rows(ai_settings,ship.rect.height,
        alien.rect.height))
    for row_counter in range(number_rows):
        for alien_counter in range(alien_numberx):
            create_alien(ai_settings,screen,aliens,alien_counter,row_counter)
        
def get_number_rows(ai_settings,ship_height,alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height - ship_height -
        (3*alien_height))
    number_rows = available_space_y / (2*alien_height)
    return number_rows
    
def update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets):
    """To make the alien fleet move on screen."""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    #for alien in aliens:
    #    alien.update()
    #Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets)

    check_aliens_bottom(ai_settings,stats,sb,screen,ship,aliens,bullets)

def ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets):
    """Respond to ship being hit by an alien."""
    if stats.ships_left > 0:
        stats.ships_left -= 1
        # update scoreboard
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings,stats,sb,screen,ship,aliens,bullets):
    """Check if aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets)
            break

def check_fleet_edges(ai_settings,aliens):
    """Respond appropriately if any of the aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break
            
def change_fleet_direction(ai_settings,aliens):
    """Drop the entire fleet and change it's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.downward_speed_factor
    ai_settings.alien_fleet_direction *= -1

def check_high_score(sb,stats):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
