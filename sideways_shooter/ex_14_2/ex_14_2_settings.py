# PCC (P.285) Ex.14-2 Target Practice.
class Settings:
    """Target Practice settings."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Ship Settings
        self.ship_speed = 2.5

        # Alien settings
        self.alien_speed = 2.0
        self.alien_limit = 3
        # Alien direction of 1 represents up; -1 represents down.
        self.alien_direction = 1

        # Bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3
