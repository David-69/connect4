import pygame
from object import *
from constants import *

class Square(Object):

    def __init__(self, x, y, status):
            
        super().__init__(x, y)

        self.status = status
        
    def draw(self, screen):
        pygame.draw.rect(screen, "white", (self.position.x, self.position.y, SQUARE_SIZE, SQUARE_SIZE))
