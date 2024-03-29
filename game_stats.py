class GameStats():
    """Keeping tab on game statistics."""
    def __init__(self,ai_settings):
        """Initialize the statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Alien Invasion in the active state.
        self.game_active = False

        # High score should never be reset.
        filename = 'high_score.txt'
        with open(filename) as fileobject1:
            contents = int(fileobject1.read())
            self.high_score = contents
        #self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        
