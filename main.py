import pygame

SCREEN_COLOR = (255, 255, 255)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
CLOCK_FREQUENCY = 1

TILES_SIZE = 20
TILES_COLOR = (0, 0, 0)


def display_checkerboard():
    k, l = int(SCREEN_HEIGHT / TILES_SIZE), int(SCREEN_WIDTH / TILES_SIZE)
    for i in range(k):
        for j in range(l):
            if (i + j) % 2 == 1:
                rect = pygame.Rect(
                    j * TILES_SIZE, i * TILES_SIZE, TILES_SIZE, TILES_SIZE
                )
                pygame.draw.rect(screen, TILES_COLOR, rect)


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
    display_checkerboard()
    pygame.display.update()

print(f"{status=}")
