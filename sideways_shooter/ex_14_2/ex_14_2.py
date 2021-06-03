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
        self.alien = pygame.sprite.Group()

        self._create_alien()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_alien()
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

    def _create_alien(self):
        """Create the alien ship."""
        # Make an alien.
        alien = Alien(self)
        self.alien.add(alien)

    def _check_alien_edges(self):
        """Respond appropriately if an alien ship reaches the screen edge."""
        for alien in self.alien.sprites():
            if alien.check_edges():
                self._change_alien_direction()
                break

    def _change_alien_direction(self):
        """Change alien ship direction when it reaches screen edge."""
        for alien in self.alien.sprites():
            alien.rect.y += self.settings.alien_speed
        self.settings.alien_direction *= -1

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update postion of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= 1200:
                self.bullets.remove(bullet)
        #print(len(self.bullets))

        self._check_bullet_alien_collison()

    def _check_bullet_alien_collison(self):
        """respond to bullet-alien ship collision."""
        # Remove bullets and alien ship when they collide.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.alien, True, True)

        if not self.alien:
            # Destroy existing bullets on screen.
            self.bullets.empty()
            # Decrement alien ships left.
            self.stats.aliens_left -= 1
            # Create a new alien ship.
            self._create_alien()

            # Pause.
            sleep(0.5)

    def _update_alien(self):
        """Update the position of the alien ship."""
        self._check_alien_edges()
        self.alien.update()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()  # Ship is drawn after background to not disappear.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.alien.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, run the game.
    tp = TargetPractice()
    tp.run_game()
