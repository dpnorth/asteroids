# pygame is an open-source library
import pygame
from constants import *
from player import *
from asteroidfield import *

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
    asteroids = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

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
        for item in asteroids:
            if item.check_collision(player):
                print("Game over!")
                return
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()
