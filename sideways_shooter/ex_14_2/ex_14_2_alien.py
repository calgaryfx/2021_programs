# PCC (P.285) Ex.14-2 Alien.
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent the alien ship."""
    def __init__(self, tp_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = tp_game.screen

        # Load the alien ship image and set its rect attribute.
        self.image = pygame.image.load('images/alien_ship.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top right of the screen.
        self.screen_rect = self.screen.get_rect()
        self.rect.midright = self.screen_rect.midright

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
