import pygame
from rectshape import RectShape
from constants import DINO_WIDTH, DINO_HEIGHT

class Dino(RectShape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = pygame.image.load("images/dino.png")
        self.image = pygame.transform.scale(self.image, (DINO_WIDTH, DINO_HEIGHT))
        self.rect = pygame.Rect(x, y, width, height)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
