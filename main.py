import pygame
import random

SCREEN_COLOR = (255, 255, 255)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
CLOCK_FREQUENCY = 5

TILES_SIZE = 20
TILES_COLOR = (0, 0, 0)

SNAKE_COLOR = (0, 255, 0)

FRUIT_COLOR = (255, 0, 0)


class Game:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

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

    def check_fruit_collision(self):
        if self.fruit.position == self.snake.position[-1]:
            self.fruit = Fruit()
            self.snake.position.insert(0, self.snake.queue)

    def update(self):
        self.snake.update()
        self.check_fruit_collision()

    def display(self):
        self.display_checkerboard()
        self.fruit.display()
        self.snake.display()


class Snake:
    def __init__(self):
        self.position = [(10, 5), (10, 6), (10, 7)]
        self.queue = self.position[0]

    def update(self):
        self.queue = self.position[0]
        self.position.append(
            (
                self.position[-1][0] + direction[0],
                self.position[-1][1] + direction[1],
            )
        )
        self.position.pop(0)

    def display(self):
        for i, j in self.position:
            x, y = i * TILES_SIZE, j * TILES_SIZE
            rect = pygame.Rect(y, x, TILES_SIZE, TILES_SIZE)
            pygame.draw.rect(screen, SNAKE_COLOR, rect)


class Fruit:
    def __init__(self):
        i = random.randint(0, int(SCREEN_HEIGHT / TILES_SIZE) - 1)
        j = random.randint(0, int(SCREEN_WIDTH / TILES_SIZE) - 1)
        self.position = (i, j)

    def display(self):
        i, j = self.position
        x, y = i * TILES_SIZE, j * TILES_SIZE
        rect = pygame.Rect(y, x, TILES_SIZE, TILES_SIZE)
        pygame.draw.rect(screen, FRUIT_COLOR, rect)


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

    game.update()
    game.display()
    pygame.display.update()

print(f"{status=}")
