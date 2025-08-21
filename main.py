import pygame
from pygame.time import Clock
from constants import*
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    updateable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updateable_group,drawable_group)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    Asteroid.containers = (asteroids,updateable_group,drawable_group)
    AsteroidField.containers = (updateable_group)
    asteroidfield = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')
        updateable_group.update(dt)
        for object in drawable_group:
            object.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()
