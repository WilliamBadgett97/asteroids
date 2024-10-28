import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        old_asteroid = self
        self.kill()
        # 
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle_one = random.uniform(20,50)
        vector_one = self.velocity.rotate(angle_one)
        vector_two = self.velocity.rotate(-angle_one)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_one = Asteroid(old_asteroid.position.x, old_asteroid.position.y, new_radius)
        new_asteroid_two = Asteroid(old_asteroid.position.x, old_asteroid.position.y, new_radius)
        new_asteroid_one.velocity = vector_one * 1.2
        new_asteroid_two.velocity = vector_two * 1.2
