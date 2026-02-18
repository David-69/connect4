import pygame
from constants import *

class Cell():

    def __init__(self, x, y, grid_position):
        self.position = pygame.Vector2(x,y)
        self.grid_position = grid_position
        
    def draw(self, screen):
        pygame.draw.rect(screen, "white", (self.position.x, self.position.y, SQUARE_SIZE, SQUARE_SIZE))
        print(f"Cell placed at {self.position}")
        pass
