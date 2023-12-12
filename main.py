import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))

clock = pygame.time.Clock()

pygame.display.set_caption("Snake")

while True:
    clock.tick(1)

    for event in pygame.event.get():
        pass

    screen.fill((255, 255, 255))

    pygame.display.update()
