import random

from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        split_angle = random.uniform(20, 50)
        split_velocity_1 = self.velocity.rotate(split_angle)
        split_velocity_2 = self.velocity.rotate(-split_angle)
        split_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.position.x, self.position.y, split_radius)
        asteroid_1.velocity = split_velocity_1 * 1.2

        asteroid_2 = Asteroid(self.position.x, self.position.y, split_radius)
        asteroid_2.velocity = split_velocity_2 * 1.2
