# PCC (P.285) Ex.14-2 Target Practice.
import pygame

class Ship:
    """A class to manage the ship on the left side of the screen."""

    def __init__(self, tp_game):
        """Initialize the ship and set its starting position."""
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.screen_rect = tp_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/rocket_small.png')
        self.rect = self.image.get_rect()

        # Start the ship on left hand side of screen, in the middle.
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the ships vertical position.
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ships position based on the movement flags."""
        # Update the ships y value, not the rect.
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Update rect object from self.y.
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the ships vertical position.
        self.y = float(self.rect.y)
