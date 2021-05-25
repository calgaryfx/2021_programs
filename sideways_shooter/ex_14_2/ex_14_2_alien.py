# PCC (P.285) Ex.14-2 Alien.
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent the alien ship."""
    def __init__(self, ss_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien_ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top right of the screen.
        self.rect.right = self.rect.width
        self.rect.top = self.rect.height

        # Store the aliens exact vertical position.
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.top <= screen_rect.top or self.rect.right <= 800:
            return True

    def update(self):
        """Move the alien down or up."""
        self.y += (self.settings.alien_speed * self_settings.fleet_direction)
        self.rect.y = self.y
        
