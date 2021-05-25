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
        self.alien = pygame.sprite.Group()

        # Make the Play button.
        self.play_button = Button(self, "Press p to play")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_alien()

            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygmae.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _start_game(self):
        """Start a new game when player clicks 'p'."""
        self.stats.reset_stats()
        self.stats.game_active = True

        # Get rid of any remaining bullets.
        self.bullets.empty()

        # Create a new alien and center the ship.
        self._create_alien()
        self.ship.center_ship()

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
        elif event.key == pygame.K_p:
            self._start_game()

    def _check_keyup_events(self):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
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
                self._shots_missed()
        # print(len(self.bullets))

        # Check for any bullets that have hit alien.
        # If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.alien, True, True)

        if not self.alien:
            # Destroy exisitng bullets and create new alien.
            self.bullets.empty()
            self._create_alien()

    def _create_alien(self, alien_number, row_number):
        """Create an alien, place it on the screen."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.rect.x = 1200 - (2 * alien_width) - (2 * alien.rect.width) * (
                        row_number)
        alien.rect.y = alien.y = alien.rect.height + 2  * alien.rect.height * (
                        alien_number)
        self.alien.add(alien)

    def _update_alien(self):
        """Change alien direction when screen edges reached."""
        self._check_alien_edges()
        self.alien.update()

    def _shots_missed(self):
        """Increment shots missed and respond to 3 shots missing alien ship."""
        if self.stats.shots_left > 1:
            # Decrement shots left.
            self.stats.shots_left -= 1

            # Get rid of remaining alien ships and bullets.
            self.alien.empty()
            self.bullets.empty()

            # Create a new alien ship.
            self._create_alien()

            # Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _update_screen(self):
        """Update images on the screen, flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.alien.draw(self.screen)

        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, run the game.
    tp = TargetPractice()
    tp.run_game()
