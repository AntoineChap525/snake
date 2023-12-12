import pygame

SCREEN_COLOR = (255, 255, 255)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
CLOCK_FREQUENCY = 1

TILES_SIZE = 20
TILES_COLOR = (0, 0, 0)

SNAKE_COLOR = (0, 255, 0)

snake_position = [(10, 5), (10, 6), (10, 7)]


def display_checkerboard():
    k, l = int(SCREEN_HEIGHT / TILES_SIZE), int(SCREEN_WIDTH / TILES_SIZE)
    for i in range(k):
        for j in range(l):
            if (i + j) % 2 == 1:
                rect = pygame.Rect(
                    j * TILES_SIZE, i * TILES_SIZE, TILES_SIZE, TILES_SIZE
                )
                pygame.draw.rect(screen, TILES_COLOR, rect)


def draw_snake(snake_position):
    for i, j in snake_position:
        x, y = i * TILES_SIZE, j * TILES_SIZE
        rect = pygame.Rect(y, x, TILES_SIZE, TILES_SIZE)
        pygame.draw.rect(screen, SNAKE_COLOR, rect)


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
    draw_snake(snake_position)
    pygame.display.update()

print(f"{status=}")
