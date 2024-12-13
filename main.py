# pygame is an open-source library
import pygame
from constants import *
from player import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    init_tup = pygame.init()
    print(f"{init_tup[0]} passed and {init_tup[1]} failed")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Gameloop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for item in updateable:
            item.update(dt)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()
