import pygame.font
import pygame

class Button():
    """A class for developing buttons in the game."""
    def __init__(self,screen,ai_settings,msg):
        """Initialize the button attributes."""
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #Set the dimensions and other properties of button.
        self.width,self.height = 200,50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        #Build button's rect and position it at center of screen.
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        #The button message needs to be prepped only once.
        self.prep_msg(msg)#calling the another method from the main.

    def prep_msg(self,msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg,True,self.text_color,
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
