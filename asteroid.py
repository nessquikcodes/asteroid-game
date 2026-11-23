import random

import pygame

import circleshape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH, ASTEROID_SPLIT_SPEEDUP
from logger import log_event


class Asteroid(circleshape.CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        movement1 = self.velocity.rotate(random_angle)
        movement2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        scaled_velocity1 = movement1 * ASTEROID_SPLIT_SPEEDUP
        scaled_velocity2 = movement2 * ASTEROID_SPLIT_SPEEDUP

        asteroid1.velocity = scaled_velocity1
        asteroid2.velocity = scaled_velocity2
