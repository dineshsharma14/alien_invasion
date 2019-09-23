import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
    """A Class for score keeping and displaying."""
    def __init__(self,ai_settings,screen,stats):
        """ Initialize the attributes of the class."""

        self.ai_settings = ai_settings
        self.screen = screen
        self.stats = stats
        self.screen_rect = screen.get_rect()

        # Instantialize the font object and other font settings.
        # To print text on the screen.
        self.font = pygame.font.SysFont(None,48)
        self.text_color = (150,100,60)
        self.text_color_level = (250,50,20)

        # Create the text image call here in __init__
        self.prep_score()

        # Create the call to high_score method
        self.prep_high_score()

        # Create the call to level method
        self.prep_level()

        # Create call to ship method
        self.prep_ships()

    def prep_score(self):
        """Turn the score into rendered image."""
        #score_str = str(self.stats.score)
        rounded_score = round(self.stats.score,-1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,self.text_color,
            self.ai_settings.bg_color)
        #Display the score at top right corner.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into rendered image."""
        high_score = int(round(self.stats.high_score,-1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,True,
            self.text_color,self.ai_settings.bg_color)
        # Center the high score at top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Turn level into a rendered image."""
        self.level_image = self.font.render(str(self.stats.level),True,
            self.text_color_level,self.ai_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings,self.screen)
            ship.rect.x = 10 +ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
            
    def show_score(self):
        """Draw the score & other aspects on the screen."""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)

        # Draw ships.
        self.ships.draw(self.screen)
        
