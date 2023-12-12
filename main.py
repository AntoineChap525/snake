import pygame

SCREEN_COLOR = (255, 255, 255)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
CLOCK_FREQUENCY = 1

TILES_SIZE = 20
TILES_COLOR = (0, 0, 0)

SNAKE_COLOR = (0, 255, 0)


class Game:
    def __init__(self):
        self.snake = Snake()

    def display_checkerboard(self):
        screen.fill(SCREEN_COLOR)
        k, l = int(SCREEN_HEIGHT / TILES_SIZE), int(SCREEN_WIDTH / TILES_SIZE)
        for i in range(k):
            for j in range(l):
                if (i + j) % 2 == 1:
                    rect = pygame.Rect(
                        j * TILES_SIZE, i * TILES_SIZE, TILES_SIZE, TILES_SIZE
                    )
                    pygame.draw.rect(screen, TILES_COLOR, rect)

    def update_snake(self):
        self.snake.position.append(
            (
                self.snake.position[-1][0] + direction[0],
                self.snake.position[-1][1] + direction[1],
            )
        )
        self.snake.position.pop(0)

    def display_snake(self):
        for i, j in self.snake.position:
            x, y = i * TILES_SIZE, j * TILES_SIZE
            rect = pygame.Rect(y, x, TILES_SIZE, TILES_SIZE)
            pygame.draw.rect(screen, SNAKE_COLOR, rect)


class Snake:
    def __init__(self):
        self.position = [(10, 5), (10, 6), (10, 7)]


game = Game()


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

    game.display_checkerboard()
    game.update_snake()
    game.display_snake()
    pygame.display.update()

print(f"{status=}")
