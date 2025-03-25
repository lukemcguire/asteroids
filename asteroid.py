import pygame

from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, pygame.Color(255, 255, 255), self.position, self.radius, 2)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
