import pygame

SCREEN_COLOR = (255, 255, 255)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
CLOCK_FREQUENCY = 1

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

pygame.display.set_caption("Snake")

while True:
    clock.tick(CLOCK_FREQUENCY)

    for event in pygame.event.get():
        pass

    screen.fill(SCREEN_COLOR)

    pygame.display.update()
