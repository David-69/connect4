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
        
        for i in range(1, GRID_SIZE_X + 1):
            self.cells[str(i)] = Cell(self.position.x + (SQUARE_DIST * (i - 1)), self.position.y, str(i))
            self.cells[str(i)].create_squares()
        
            
    def draw(self, screen):
        pygame.draw.rect(screen, GREY, (self.position.x - 20, self.position.y - 20, GRID_OUTLINE.x, GRID_OUTLINE.y), LINE_WIDTH + 1, (SQUARE_SIZE // 2))
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        # Number keys to select cells:
        if keys[pygame.K_1]:
            for cell in self.cells:
                self.cells[cell].deselect()
            self.cells["1"].select()
        if keys[pygame.K_2]:
            for cell in self.cells:
                self.cells[cell].deselect()
            self.cells["2"].select()
        if keys[pygame.K_3]:
            for cell in self.cells:
                self.cells[cell].deselect()
            self.cells["3"].select()
        if keys[pygame.K_4]:
            for cell in self.cells:
                self.cells[cell].deselect()
            self.cells["4"].select()
        if keys[pygame.K_5]:
            for cell in self.cells:
                self.cells[cell].deselect()
            self.cells["5"].select()
        if keys[pygame.K_6]:
            for cell in self.cells:
                self.cells[cell].deselect()
            self.cells["6"].select()
        if keys[pygame.K_7]:
            for cell in self.cells:
                self.cells[cell].deselect()
            self.cells["7"].select()
        
        if keys[pygame.K_RETURN]:
            for cell in self.cells:
                if self.cells[cell].selected == True:
                    self.cells[cell].drop_piece("red")
                    self.cells[cell].deselect()