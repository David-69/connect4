import pygame
import arrow
from object import *
from constants import *
from square import *
from arrow import *
from string import ascii_lowercase

class Cell(Object):

    def __init__(self, x, y, label):
        
        super().__init__(x, y)

        self.squares = {}
        self.label = label
        self.selected = False
        self.arrow = []

    
    def create_squares(self):
        
        for i in range(GRID_SIZE_Y):
            self.squares[ascii_lowercase[i]] = Square(self.position.x, self.position.y + (SQUARE_DIST * i), "empty")

    def add_label(self, screen):
        font = pygame.font.SysFont("Arial", 16)
        text = font.render(self.label, True, WHITE)
        screen.blit(text, (self.position.x + (SQUARE_SIZE // 2) - (text.get_width() // 2), self.position.y - 43))

    def select(self):
        self.selected = True
    
    def deselect(self):
        self.selected = False

    def update(self, dt):
        if self.selected == True:
            self.arrow.append(Arrow(self.position.x + (SQUARE_SIZE // 2), self.position.y - 50))
        elif self.selected == False:
            for arrow in self.arrow:
                arrow.kill()
            self.arrow = []
    
    def drop_piece(self, color):
        for square in reversed(self.squares.values()):
            if square.status == "empty":
                square.status = color
                break