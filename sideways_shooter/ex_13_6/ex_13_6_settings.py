class Settings:
    """A class to store all the settings for Sideways Shooter."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings.
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings.
        self.bullet_speed = 3.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 33

        # Alien settings
        self.alien_speed = 2
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents up, -1 represents down.
        self.fleet_direction = 1
