import pygame
import numpy as np

# Define the polynomial function whose roots we want to find


def f(x):
    return x**3 - 3*x + 1

# Define the derivative of the polynomial function


def df(x):
    return 3*x**2 - 3

# Define the function that implements Newton's method


def newton(x0, f, df, tol, max_iter):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        dfx = df(x)
        if dfx == 0:
            break
        x = x - fx/dfx
    return None


# Define some constants
WIDTH = 640
HEIGHT = 480
X_MIN = -5
X_MAX = 5
Y_MIN = -5
Y_MAX = 5
MAX_ITER = 20
TOL = 1e-6

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Newton's Method")

# Define the color palette
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define the function that maps screen coordinates to graph coordinates


def screen_to_graph(pos):
    x = X_MIN + (X_MAX - X_MIN)*pos[0]/WIDTH
    y = Y_MAX - (Y_MAX - Y_MIN)*pos[1]/HEIGHT
    return (x, y)

# Define the function that maps graph coordinates to screen coordinates


def graph_to_screen(pos):
    x = int(WIDTH*(pos[0] - X_MIN)/(X_MAX - X_MIN))
    y = int(HEIGHT*(Y_MAX - pos[1])/(Y_MAX - Y_MIN))
    return (x, y)


# Main loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = screen_to_graph(pygame.mouse.get_pos())
            root = newton(pos[0], f, df, TOL, MAX_ITER)
            if root is not None:
                print("Found root at", root)
                screen_pos = graph_to_screen((root, 0))
                pygame.draw.circle(screen, GREEN, screen_pos, 5)

    # Clear the screen
    screen.fill(WHITE)

    # Draw the x and y axes
    pygame.draw.line(screen, BLACK, graph_to_screen(
        (0, Y_MIN)), graph_to_screen((0, Y_MAX)))
    pygame.draw.line(screen, BLACK, graph_to_screen(
        (X_MIN, 0)), graph_to_screen((X_MAX, 0)))

    # Draw the polynomial function
    xs = np.linspace(X_MIN, X_MAX, 1000)
    ys = f(xs)
    points = np.array([graph_to_screen((xs[i], ys[i]))
                      for i in range(len(xs))])
    pygame.draw.lines(screen, BLUE, False, points, 2)

    # Update the screen
    pygame.display.update()
