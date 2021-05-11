import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien iin the fleet."""
    def __init__(self, ss_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top right of the screen.
        self.rect.right = self.rect.width
        self.rect.top = self.rect.height

        # Store the alien's exact vertical position.
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.top <= screen_rect.top or self.rect.right <= 800:
            return True

    def update(self):
        """Move the alien down or up."""
        self.y += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.y = self.y


"""In Pygame, the Rect object has virtual attributes which can be used to move
and align the Rect:
x,y
top, left, bottom, right
topleft, bottomleft, topright, bottomright
midtop, midleft, midbottom, midright
center, centerx, centery
size, width, height
w,h

All of those attributes can be assigned to:
rect1.right = 10
rect2.center = (20, 30)

Info from:
https://www.pygame.org/docs/ref/rect.html?highlight=midtop
"""
