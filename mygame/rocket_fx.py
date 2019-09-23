import pygame,sys
from bullet import Bullet

def check_keydown_events(event,r_settings,screen,rocket,bullets):
    """Respond to the keypresses"""
    if event.key == pygame.K_RIGHT:
        #(earlier code)rocket.rect.centerx += 1
        #flag setting changed
        rocket.moving_right = True
                        
    if event.key == pygame.K_LEFT:
        rocket.moving_left = True

    if event.key == pygame.K_UP:
        rocket.moving_up = True

    if event.key == pygame.K_DOWN:
        rocket.moving_down = True

    if event.key == pygame.K_SPACE:
        fire_bullet(r_settings,screen,rocket,bullets)

def fire_bullet(r_settings,screen,rocket,bullets):
    """Fire bullet if limit not reached yet"""
    #Create a bullet and add it to bullets group
    if len(bullets)< r_settings.bullet_count:
        new_bullet = Bullet(r_settings,rocket,screen)
        bullets.add(new_bullet)

def check_keyup_events(event,rocket):

        if event.key == pygame.K_RIGHT:
            rocket.moving_right = False

        if event.key == pygame.K_LEFT:
            rocket.moving_left = False

        if event.key == pygame.K_UP:
            rocket.moving_up = False

        if event.key == pygame.K_DOWN:
            rocket.moving_down = False

def checkevents(r_settings,screen,rocket,bullets):
    #Fx checking keyboard and mouse events. 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,r_settings,screen,rocket,bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,rocket) 

def update_screen(r_settings,screen,rocket,bullets):
    #Fx for updating the game screen.
    screen.fill(r_settings.bg_color) 
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    rocket.blitme()
    pygame.display.flip()

def update_bullets(bullets):
    #Fx to update bullets and get rid of once already fired.
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #print(len(bullets))
