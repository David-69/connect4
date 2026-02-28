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
        
        for i in range(GRID_SIZE_Y):
            self.squares[ascii_lowercase[i]] = Square(self.position.x, self.position.y + (SQUARE_DIST * i), "red")

    def add_label(self, screen):
        font = pygame.font.SysFont("Arial", 16)
        text = font.render(self.label, True, WHITE)
        screen.blit(text, (self.position.x + (SQUARE_SIZE // 2) - (text.get_width() // 2), self.position.y - 20))
