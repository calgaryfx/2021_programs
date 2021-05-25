# PCC (P.285) Ex.14-2 Target Practice.
import pygame

class Ship:
    """A class to manage the ship on the left side of the screen."""

    def __init__(self, ss_game):
        """Initialize the ship and set its starting position."""
        self.screen = ss_game.screen
        
