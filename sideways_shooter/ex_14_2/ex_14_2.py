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
        
