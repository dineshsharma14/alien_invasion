import pygame

class Rocket():
    """Rocket design and functionalities"""
    
    def __init__(self,screen):
        """Initialization of the class and variables below"""
        self.screen = screen
        #self.r_settings = r_settings
        #Loading the rocket image and getting respective rects
        self.image = pygame.image.load('rocketimage/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #Setting the flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
        #Taking the image at center of the screen
        self.rect.center = self.screen_rect.center

        #To fine speed control of the rocket
        self.center1 = float(self.rect.centerx)
        self.center2 = float(self.rect.centery)

    def update(self,r_settings):
        """Method for the continuous movement of rocket image"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center1 += r_settings.rocket_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center1 -= r_settings.rocket_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.center2 -= r_settings.rocket_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center2 += r_settings.rocket_speed_factor

        #Update rect object from self.center1 and 2
        self.rect.centerx = self.center1
        self.rect.centery = self.center2

    def blitme(self):
        """A method to display the image on screen"""
        self.screen.blit(self.image,self.rect)
        
        

        
