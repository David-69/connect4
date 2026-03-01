import pygame
from object import *
from constants import *

class Arrow(Object):

    def __init__(self, x, y,):
            
        super().__init__(x, y)

    def arrow(self):
        a = self.position
        b = (a.x + 6, a.y - 5)
        c = (a.x + 2, a.y - 5)
        d = (a.x + 2, a.y - 14)
        e = (a.x - 2, a.y - 14)
        f = (a.x - 2, a.y - 5)
        g = (a.x - 6, a.y - 5)

        return [a, b, c, d, e, f, g]
        
    def draw(self, screen):
        pygame.draw.polygon(screen, WHITE, self.arrow())