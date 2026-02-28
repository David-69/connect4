import pygame
from object import *
from square import *
from constants import *
from cell import *

class Grid(Object):

    def __init__(self, x, y):

        super().__init__(x, y)

        self.cells = {}
    
    def create_cells(self):

        self.position.y = 150
        
        for i in range(GRID_SIZE_X + 1):
            self.cells[str(i + 1)] = Cell(self.position.x + (SQUARE_DIST * i), self.position.y, str(i + 1))
            self.cells[str(i + 1)].create_squares()
            
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.position.x - 3, self.position.y - 3, (SQUARE_DIST * (GRID_SIZE_Y)) + 6, (SQUARE_DIST * (GRID_SIZE_X)) + 6), LINE_WIDTH)
    

