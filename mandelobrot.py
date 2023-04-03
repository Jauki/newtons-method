import pygame
import numpy as np
import imageio

counter = 0


def mandelbrot(c, max_iter):
    # print(f'Iteration: {counter}')
    # counter += 1
    z = 0
    for i in range(max_iter):
        z = z**2 + c
        if abs(z) > 2:
            return i
    return max_iter


WIDTH = 640*3
HEIGHT = 480*3
X_MIN = -2
X_MAX = 1
Y_MIN = -1
Y_MAX = 1
MAX_ITER = 1000


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mandelbrot Set")

PALETTE = [
    (66, 30, 15), (25, 7, 26), (9, 1, 47), (4, 4, 73), (0, 7, 100),
    (12, 44, 138), (24, 82, 177), (57, 125, 209), (134, 181, 229),
    (211, 236, 248), (241, 233, 191), (248, 201, 95), (255, 170, 0),
    (204, 128, 0), (153, 87, 0), (106, 52, 3)
]

mandelbrot_set = np.zeros((WIDTH, HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill((255, 255, 255))
    for i in range(WIDTH):
        for j in range(HEIGHT):
            x = X_MIN + (X_MAX - X_MIN)*i/WIDTH
            y = Y_MIN + (Y_MAX - Y_MIN)*j/HEIGHT
            c = complex(x, y)
            n = mandelbrot(c, MAX_ITER)
            color = PALETTE[n % len(PALETTE)]
            mandelbrot_set[i, j] = n
            pygame.draw.rect(screen, color, (i, j, 1, 1))

    mandelbrot_set = mandelbrot_set / MAX_ITER
    imageio.imwrite("mandelbrot_set.png", mandelbrot_set)
    pygame.display.update()
