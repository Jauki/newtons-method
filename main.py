import pygame
import sys
import numpy as np


window_size = (500, 500)
pygame.init()
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Newton Method - Fractal")


coefficients = [1, 0, 0, -1]
p = np.poly1d(coefficients)
dp = p.deriv()


X_MIN, X_MAX, Y_MIN, Y_MAX = -2, 2, -2, 2
WIDTH, HEIGHT = 500, 500
tolerance = 1e-20
max_iterations = 1
roots = [complex(1, 0)]
color_map = np.zeros((WIDTH, HEIGHT, 3), dtype=np.uint8)


x = np.linspace(X_MIN, X_MAX, WIDTH)
y = np.linspace(Y_MIN, Y_MAX, HEIGHT)
z = x[:, np.newaxis] + y[np.newaxis, :]*1j

for i in range(max_iterations):
    dz = np.where(dp(z) != 0, p(z) / dp(z), tolerance)
    z = z - dz
    root_index = np.abs(z.reshape(-1, 1) -
                        np.array(roots).reshape(1, -1)).argmin(axis=1)
    is_new_root = np.abs(dz) > tolerance
    new_roots = np.where(is_new_root, z, 0)
    new_root_index = np.where(is_new_root, len(roots), 0)
    roots += list(new_roots[new_root_index])
    color_map[is_new_root] = new_root_index[new_root_index >
                                            0][:, np.newaxis] * np.array([10, 20, 30])[np.newaxis, :]


screen.blit(pygame.surfarray.make_surface(color_map.swapaxes(0, 1)), (0, 0))
print("UPDATE")
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
