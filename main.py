import pygame
from constants import * 
from grid import *
from square import *   
from cell import *


def main():

    # Groups:
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    cells = pygame.sprite.Group()
    squares = pygame.sprite.Group()
    grids = pygame.sprite.Group()


    # Group Allocation:
    Cell.containers = (cells, updatable, drawable)
    Square.containers = (squares, updatable, drawable)
    Grid.containers = (grids, updatable, drawable)

    # Load Pygame:
    pygame.init()

    # Defining stuff:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    grid = Grid(150, 150)
    grid.create_cells()

    #Game Loop:
    while True:
        # Logs:
        ## A good place to put logs if you need them maybe?


        # Exit game when window closes:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill Background:
        screen.fill("black")



        # ***Process***:
        updatable.update(dt)

        for sprite in drawable:
            sprite.draw(screen)

        for cell in cells:
            cell.add_label(screen)

        # Frame cycling I think?
        pygame.display.flip()
        
        # Rate:
        clock.tick(60)
        dt = (clock.get_time() / 1000)

        


# Main: 
if __name__ == "__main__":
    main()
