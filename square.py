import pygame
from object import *
from constants import *

class Square(Object):

    states = {
            "empty": {
                "color": WHITE
            },
            "red": {
                "color": RED
            },
            "yellow": {
                "color": YELLOW
            }
        }
    

    def __init__(self, x, y, status):
            
        super().__init__(x, y)

        self.status = status
        
    def draw(self, screen):
        #pygame.draw.rect(screen, WHITE, (self.position.x - 3, self.position.y - 3, SQUARE_SIZE + 6, SQUARE_SIZE + 6), LINE_WIDTH)
        if self.status != "empty":
            pygame.draw.circle(screen, self.states[self.status]["color"], (self.position.x + (SQUARE_SIZE // 2), self.position.y + (SQUARE_SIZE // 2)), (SQUARE_SIZE // 2) - LINE_WIDTH)
        pygame.draw.circle(screen, WHITE, (self.position.x + (SQUARE_SIZE // 2), self.position.y + (SQUARE_SIZE // 2)), (SQUARE_SIZE // 2) - LINE_WIDTH, LINE_WIDTH)
        
