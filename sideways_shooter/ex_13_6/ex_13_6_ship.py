import pygame

class ShipLeft:
    """A class to manage the ship when on left side of screen."""

    def __init__(self, ss_game):
        """Initialize the ship and set its starting position."""
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.screen_rect = ss_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship_left.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the middle left of the screen.
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
