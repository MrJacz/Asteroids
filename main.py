import pygame
from asteroid import Asteroid
from constants import *
from player import *
from asteroidfield import *
from sys import exit

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # pygame stuff
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)

    af = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)

        for d in drawable:
            d.draw(screen)

        pygame.display.update()

        for ent in asteroids:
            if not ent.check_collision(player):
                print("Game over!")
                exit()


        dt = clock.tick(SCREEN_FPS) / 1000

if __name__ == "__main__":
    main()
