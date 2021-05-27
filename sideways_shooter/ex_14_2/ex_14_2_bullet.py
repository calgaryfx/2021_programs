# PCC (P.285) Ex.14-2 Bullet.
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, tp_game):
        """Create a bullet objective at the ships current position."""
        
