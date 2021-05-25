# PCC (P.285) Ex.14-2 Target Practice.
# Create ship on right side that moves up and down at a asteady rate.
# Create ship on left side player can move up and down and fire bullets.
# Add a play button that starts the game, after the player misses the target three
# times, end the game, have play button re-appear to re-start.
import pygame

from ex_14_2_settings import Settings

class SidewaysShooter:
    """Overall class to manage game assets and behavior."""

    def _init_(self):
        """Initialize the game, create game resources."""
        pygame.init()
        self.setting = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Sideways Shooter Ex.14-2")

        # Create an instance to store game statistics.
        self.stats = GameStats(self)
        
