import pygame
from constants import *

def main():

    # Load Pygame:
    pygame.init()

    # Defining stuff:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Groups:
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Group Allocation:
    ## Put things in groups here...

    #Game Loop:
    while True:
        
        # Logs:
        ## A good place to put logs if you need them maybe?

        # Exit game when window closes:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill Background:
        screen.fill("red")

        # ***Process***:
        updatable.update(dt)


        # Frame cycling I think?
        pygame.display.flip()
        
        # Rate:
        clock.tick(60)
        dt = (clock.get_time() / 1000)

        


# Main: 
if __name__ == "__main__":
    main()
