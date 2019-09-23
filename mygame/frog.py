import pygame

class Frog():
    def __init__(self,screen):
        self.screen = screen

        self.image = pygame.image.load('rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        # getting frog on center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.center = self.screen_rect.center

        #Initializing the movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):

        if self.moving_right:
            self.rect.centerx += 1

        if self.moving_left:
            self.rect.centerx -= 1

        if self.moving_up:
            self.rect.top += 1

        if self.moving_down:
            self.rect.top -= 1
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)

        
