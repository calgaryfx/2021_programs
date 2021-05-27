# PCC (P.285) Ex.14-2 Target Practice.
# Create ship on right side that moves up and down at a asteady rate.
# Create ship on left side player can move up and down and fire bullets.
# Add a play button that starts the game, after the player misses the target three
# times, end the game, have play button re-appear to re-start.
import sys
from time import sleep

import pygame

from ex_14_2_settings import Settings
from ex_14_2_game_stats import GameStats
from ex_14_2_button import Button
from ex_14_2_ship import Ship
from ex_14_2_bullet import Bullet
from ex_14_2_alien import Alien

class TargetPractice:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Target Practice")

        # Create an instance to store game statistics.
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()

            self._update_screen()

    def _check_events(self):
        """Respond to keypress events."""
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
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared off the screen.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= 1200:
                self.bullets.remove(bullet)
        #print(len(self.bullets))

        # Check for any bullets that have hit the alien.
        # If so, get rid of the bullet and alien.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.alien, True, True)

        if not self.alien:
            # Destroy exising bullets and create new alien.
            self.bullets.empty()
            self._create_alien()

    def _update_screen(self):
        """Update images on the screen, flip to a new screen."""
        self.screen.fill(self.settings.bg_color)

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance and run the game.
    tp = TargetPractice()
    tp.run_game()
