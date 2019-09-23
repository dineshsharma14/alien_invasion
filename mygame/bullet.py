import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Bullet functionality class"""
    def __init__(self,r_settings,rocket,screen):
        super().__init__() #So that Bullet class inherits properly from Sprite
        self.screen = screen

        #Making bullet and positioning rightly
        self.rect = pygame.Rect(0,0,r_settings.bullet_width,
            r_settings.bullet_height)
        self.rect.centerx = rocket.rect.centerx
        self.rect.bottom = rocket.rect.top

        #Getting the float y coordinate of bullet
        self.y = float(self.rect.y)

        #Initializing other attributes to be used methods downstreme
        self.color = r_settings.bullet_color
        self.speed_factor = r_settings.bullet_speed_factor

    def update(self):
        """Updating the position of bullet once space bar press detected"""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """Drawing the bullet position"""
        pygame.draw.rect(self.screen,self.color,self.rect)
        
        
        
    
