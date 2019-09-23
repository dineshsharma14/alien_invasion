import pygame
from rocket_fight_settings import Settings
from rocket import Rocket
import rocket_fx as rf
from pygame.sprite import Group

def game_temp():
    pygame.init()
    r_settings = Settings()
    screen = pygame.display.set_mode((r_settings.screen_width,
        r_settings.screen_height))
    pygame.display.set_caption("Rocket Fight")

    #Make rocket instance
    rocket = Rocket(screen)

    #Make bullets instance 
    bullets = Group()

    while True:
        rf.checkevents(r_settings,screen,rocket,bullets)
        rocket.update(r_settings)
        rf.update_bullets(bullets)
        rf.update_screen(r_settings,screen,rocket,bullets)

game_temp()
