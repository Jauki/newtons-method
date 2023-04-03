import pygame
import sys
import numpy as np
import pygame_gui

window_size = (500, 500)
pygame.init()


screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Newton Method - Fractal")


bg_color = (255, 255, 255)
screen.fill(bg_color)


# clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # pygame.display.update()
