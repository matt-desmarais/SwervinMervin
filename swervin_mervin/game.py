import pygame, sys, os
from pygame.locals import *
import settings as s

class Game:
    """Represents the overall game flow"""

    def __init__(self, window, player, level):
        self.window = window
        self.player = player
        self.level  = level

    def setup(self):
        pass

    def progress(self):
        """Animate the next frame"""
        pass

    def finished(self):
        return False  

    def high_score(self):
        return False

    def game_over(self):
        """Puts the game in 'Game Over' mode"""
        pass

    def clean(self):
        pass
