import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to create one alien of the fleet"""
    def __init__(self,screen,ai_settings):
        """Initializing the class converting parameters into attributes"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Loading the image of the alien and working on its rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Placing the rect at desired location on screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        """A method to display the image on screen"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        """A method to update alien's position and make them move"""
        self.x += (self.ai_settings.alien_speed_factor *
            self.ai_settings.alien_fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """A method to check if alien fleet have touched the edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
            
