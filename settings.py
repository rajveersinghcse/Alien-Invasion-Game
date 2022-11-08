class Settings:
    """ A class to store all settinsg for alien invasion"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5

        # bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 2
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
