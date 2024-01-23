import pygame
import graphic_vars
from pygame.locals import *
from graphic_vars import*

def init():
    pygame.init()
    screen = pygame.display.set_mode((400,600))
    clock = pygame.time.Clock()
    running = True
    
    pygame.display.set_caption('Python Project')
    pygame.display.set_icon(pygame.image.load(start_icon))
    
    while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # fill the screen with a color to wipe away anything from last frame
            screen.fill("#F2F0E5")

            # RENDER YOUR GAME HERE

            # flip() the display to put your work on screen
            pygame.display.flip()

            clock.tick(60)  # limits FPS to 60

pygame.quit()


def main():
    
    init()
    

if __name__ == "__main__":
    main()   