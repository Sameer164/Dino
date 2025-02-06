import pygame, random
from constants import *
from dino import Dino
from pebble import Pebble
from cactus import Cactus


def main():   
    pygame.init()
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    clock = pygame.time.Clock()
    pause = 40
    
    speed = 10
    fast_interval = 50000 # Make the game faster every 50000 miliseconds

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    cactus = pygame.sprite.Group()

    Dino.containers = [updatables, drawables]
    Pebble.containers = [updatables, drawables]
    Cactus.containers = [cactus, updatables, drawables]

    dino = Dino(DINO_WIDTH, MAX_HEIGHT//2, DINO_WIDTH, DINO_HEIGHT)

    for _ in range(NUM_PEBBLES):
        Pebble(random.randint(*PEBBLE_X_RANGE), PEBBLE_Y, random.randint(*PEBBLE_WIDTH_RANGE), random.randint(*PEBBLE_HEIGHT_RANGE))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # pygame.time.get_ticks() gets the time passed in miliseconds since pygame.init()
        if pygame.time.get_ticks() % fast_interval == 0:
            speed *= 1.2
            pause = max(10, pause-5)
        
        if random.random() < 0.01: # Spawn a cactus at a random place
            width = random.randint(*CACTUS_WIDTH_RANGE)
            height = random.randint(*CACTUS_HEIGHT_RANGE)
            y = LINE_POSITION_Y - height
            x = MAX_WIDTH - width - 10
            Cactus(x, y, width, height)


        screen.fill("black")
        pygame.draw.line(screen, "white", (0, LINE_POSITION_Y), (MAX_WIDTH, LINE_POSITION_Y))
        updatables.update(speed)
        for obj in drawables:
            obj.draw(screen)
        pygame.display.flip()
        clock.tick(pause)  # Pauses for 1/pause th of a second and returns the time passed since last call in dt

if __name__ == "__main__":
    main()
