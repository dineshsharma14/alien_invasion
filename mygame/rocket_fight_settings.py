class Settings():
    """all the game settings in one class"""
    def __init__(self):
        #Screen settings        
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_color = (100,180,100)

        #Rocket settings
        self.rocket_speed_factor = 1.5

        #Bullet settings
        self.bullet_width = 5
        self.bullet_height = 9
        self.bullet_color = (60,30,30)
        self.bullet_speed_factor = 1
        self.bullet_count = 3

