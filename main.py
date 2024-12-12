# pygame is an open-source library
import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    init_tup = pygame.init()
    print(f"{init_tup[0]} passed and {init_tup[1]} failed")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000000)
        pygame.display.flip()
    
if __name__ == "__main__":
    main()
