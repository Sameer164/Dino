import pygame
from rectshape import RectShape
from constants import DINO_WIDTH, DINO_HEIGHT, DINO_JUMP_HEIGHT, LINE_POSITION_Y, DINO_JUMP_INTERVAL

class Dino(RectShape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = pygame.image.load("images/dino.png")
        self.image = pygame.transform.scale(self.image, (DINO_WIDTH, DINO_HEIGHT))
        self.jump_interval = -DINO_JUMP_INTERVAL
        self.jump_event_ended = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def update(self, speed):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.jump_event_ended = False
        
        if not self.jump_event_ended:
            if (self.jump_interval < 0 and LINE_POSITION_Y - DINO_JUMP_HEIGHT - DINO_HEIGHT < self.position.y) or (self.jump_interval > 0 and self.position.y < LINE_POSITION_Y - DINO_HEIGHT):
                self.position += pygame.Vector2(0, self.jump_interval)
                self.rect = pygame.Rect(self.position.x, self.position.y, self.width, self.height)
            
            if self.position.y <= LINE_POSITION_Y - DINO_JUMP_HEIGHT - DINO_HEIGHT:
                self.jump_interval = DINO_JUMP_INTERVAL
            if self.position.y >= LINE_POSITION_Y - DINO_HEIGHT:
                self.jump_interval = -DINO_JUMP_INTERVAL
                self.jump_event_ended = True
