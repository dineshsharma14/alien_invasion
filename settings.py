class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen Settings
        self.screen_width = 1100
        self.screen_height = 620
        self.bg_color = (230,230,230)

        # Ship settings
        self.ship_limit = 2

        # Bullet settings
        self.bullet_width = 4
        self.bullet_height = 8
        self.bullet_color = 60,60,60
        self.bullets_allowed = 4

        # Alien settings
        self.downward_speed_factor = 15

        # How quickly game speeds up
        self.speedup_scale = 1.2
        self.initialize_dynamic_settings()

        # How quickly the alien point values increase
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.1
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 0.3

        # fleet_direction of 1 represents right; -1 represents left.
        self.alien_fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings & alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        
    
