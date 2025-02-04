import pygame
from constants import MAX_WIDTH, MAX_HEIGHT


def main():   
    pygame.init()
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()
