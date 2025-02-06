import pygame

class RectShape(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)

    
    def update(self, dt):
        pass

    def draw(self, screen):
        pass
    
    def has_collided(self, other_rect):
        return self.position.x <= other_rect.position.x + other_rect.width \
            and self.position.x + self.width >= other_rect.position.x \
            and self.position.y <= other_rect.position.y + other_rect.height \
            and self.position.y + self.height >= other_rect.position.y
    
