import pygame
from constants import MAX_WIDTH, MAX_HEIGHT, DINO_WIDTH, DINO_HEIGHT, LINE_POSITION_Y
from dino import Dino


def main():   
    pygame.init()
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    dino = Dino(MAX_WIDTH//2, MAX_HEIGHT//2, DINO_WIDTH, DINO_HEIGHT)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.draw.line(screen, "white", (0, LINE_POSITION_Y), (MAX_WIDTH, LINE_POSITION_Y))
        dino.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
