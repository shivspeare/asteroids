import circleshape
import pygame
import random
import constants

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        rand_angle = random.uniform(20, 50)
        velocity_1 = self.velocity.rotate(rand_angle)
        velocity_2 = self.velocity.rotate(-rand_angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = velocity_1 * 1.2
        a2.velocity = velocity_2

