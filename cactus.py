import pygame
from rectshape import RectShape

class Cactus(RectShape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = pygame.image.load("images/dino.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.velocity = pygame.Vector2(-1, 0)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, speed):
        self.position += self.velocity * speed
        if self.position.x <= 0:
            self.kill()
            return
        self.rect = pygame.Rect(self.position.x, self.position.y, self.width, self.height)

