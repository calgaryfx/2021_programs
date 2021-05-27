# PCC (P.285) Ex.14-2 Alien.
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent the alien ship."""
    def __init__(self, tp_game):
        """Initialize the alien and set its starting position."""
