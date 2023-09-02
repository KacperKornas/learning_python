import sys
import pygame


screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("12-4. Keys")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print(pygame.K_RIGHT)

            if event.key == pygame.K_LEFT:
                print(pygame.K_LEFT)

            if event.key == pygame.K_UP:
                print(pygame.K_UP)

            if event.key == pygame.K_DOWN:
                print(pygame.K_DOWN)

    pygame.display.flip()