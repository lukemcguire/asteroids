import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from player import Player


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt: float = 0

    # initialize groups and assign class containers
    updatable: pygame.sprite.Group = pygame.sprite.Group()
    drawable: pygame.sprite.Group = pygame.sprite.Group()
    asteroids: pygame.sprite.Group = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    # initialize player and asteroid field
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    AsteroidField()

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_detected(player):
                print("Game over!")
                sys.exit()

        screen.fill(pygame.Color(0, 0, 0))

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        # limit framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
