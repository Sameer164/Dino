import pygame
from rectshape import RectShape
from constants import MAX_WIDTH

class Pebble(RectShape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.velocity = pygame.Vector2(-1, 0)
    
    def draw(self, screen):
        pygame.draw.rect(screen, "white", self.rect, width = 0)

    def update(self, dt):
        self.position += self.velocity * dt
        if self.position.x <= 0:
            self.position.x = MAX_WIDTH + self.position.x
        self.rect = pygame.Rect(self.position.x, self.position.y, self.width, self.height)

