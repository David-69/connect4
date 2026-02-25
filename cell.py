import pygame
from object import *
from constants import *
from square import *
from string import ascii_lowercase

class Cell(Object):

    def __init__(self, x, y, label):
        
        super().__init__(x, y)

        self.squares = {}
        self.label = label
    
    def create_squares(self):
        
        for i in range(GRID_SIZE_Y + 1):
            self.squares[ascii_lowercase[i]] = Square(self.position.x, self.position.y + (SQUARE_DIST * i), "empty")

