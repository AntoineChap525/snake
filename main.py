import pygame

SCREEN_COLOR = (255, 255, 255)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
CLOCK_FREQUENCY = 1

status = 1  # 1 when running, 0 to stop

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

pygame.display.set_caption("Snake")

while status:
    clock.tick(CLOCK_FREQUENCY)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:  # quit the game
                status = 0
        if event.type == pygame.QUIT:  # quit the game
            status = 0

    screen.fill(SCREEN_COLOR)

    pygame.display.update()

print(f"{status=}")
