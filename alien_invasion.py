import pygame 
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    """ Initialize game and create a screen object"""
    
    pygame.init() # initializes the background settings for pygame
    ai_settings = Settings()# instance of Settings class
    # Creating screen object called surface
    screen = pygame.display.set_mode((ai_settings.screen_width,
        ai_settings.screen_height)) 
    pygame.display.set_caption("Alien Invasion")

    #Make the play button.
    play_button = Button(screen,ai_settings,"Play")
    
    #Make a ship
    ship = Ship(ai_settings,screen)

    #Make a instance for game statistics and create scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    
    #Make a group of bullets in.
    bullets = Group()

    #Make a group of aliens.
    aliens = Group()
    
    gf.create_fleet(ai_settings,screen,ship,aliens)
    
    # The main while loop of the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,
            bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,sb,stats,bullets,aliens)
            gf.update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,
            play_button)
run_game()