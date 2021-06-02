# PCC (P.285) Ex.14-2 Target Practice.
import pygame

class Ship:
    """A class to manage the ship on the left side of the screen."""

    def __init__(self, tp_game):
        """Initialize the ship and set its starting position."""
        self.screen = tp_game.screen
        self.screen_rect = tp_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/rocket_small.png')
        self.rect = self.image.get_rect()

        # Start each new ship at the left side/center of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_up:
            self.rect.y -= 3
        if self.moving_down:
            self.rect.y += 3

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
