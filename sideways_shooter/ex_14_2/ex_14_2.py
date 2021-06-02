# PCC (P.285) Ex.14-2 Target Practice.
# Create ship on right side that moves up and down at a asteady rate.
# Create ship on left side player can move up and down and fire bullets.
# Add a play button that starts the game, after the player misses the target three
# times, end the game, have play button re-appear to re-start.
import sys

import pygame

from ex_14_2_settings import Settings
from ex_14_2_ship import Ship

class TargetPractice:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Target Practice")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()  # Ship is drawn after background to not disappear.

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, run the game.
    tp = TargetPractice()
    tp.run_game()
