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
    screen.fill(SCREEN_COLOR)
    k, l = int(SCREEN_HEIGHT / TILES_SIZE), int(SCREEN_WIDTH / TILES_SIZE)
    for i in range(k):
        for j in range(l):
            if (i + j) % 2 == 1:
                rect = pygame.Rect(
                    j * TILES_SIZE, i * TILES_SIZE, TILES_SIZE, TILES_SIZE
                )
                pygame.draw.rect(screen, TILES_COLOR, rect)


def draw_snake():
    for i, j in snake_position:
        x, y = i * TILES_SIZE, j * TILES_SIZE
        rect = pygame.Rect(y, x, TILES_SIZE, TILES_SIZE)
        pygame.draw.rect(screen, SNAKE_COLOR, rect)


def change_snake_position():
    snake_position.append(
        (snake_position[-1][0] + direction[0], snake_position[-1][1] + direction[1])
    )
    snake_position.pop(0)


status = 1  # 1 when running, 0 to stop
direction = (0, 1)

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

            # DIRECTION
            if event.key == pygame.K_UP:
                direction = (-1, 0)
            if event.key == pygame.K_DOWN:
                direction = (1, 0)
            if event.key == pygame.K_LEFT:
                direction = (0, -1)
            if event.key == pygame.K_RIGHT:
                direction = (0, 1)

        if event.type == pygame.QUIT:  # quit the game
            status = 0

    display_checkerboard()
    change_snake_position()
    draw_snake()

    pygame.display.update()

print(f"{status=}")
