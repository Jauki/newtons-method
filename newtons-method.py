import numpy as np


def newton(p, dp, z0):
    z = z0
    for i in range(max_iterations):
        dz = p(z) / dp(z) if dp(z) != 0 else 1e-6
        z = z - dz
        if abs(dz) < tolerance:
            return z
    return np.nan


if __name__ == "__main__":
    coefficients = [1, 0, 0, -1]
    max_iterations = 100
    tolerance = 1e-5
    p = np.poly1d(coefficients)
    dp = p.deriv()
    roots = []

    for z0 in np.arange(-10, 10, 0.5):
        root = newton(p, dp, z0)
        if not np.isnan(root):
            roots.append(root)

    print("Roots:", roots)
