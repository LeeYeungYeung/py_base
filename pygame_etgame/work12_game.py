import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Alien Invasion")

while True:
    screen.fill((0, 0, 255))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

