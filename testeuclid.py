import matplotlib.pyplot as plt

def plot_triangle(points):
    """Plots a triangle given its vertices."""
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    plt.plot(x + [x[0]], y + [y[0]], marker='o')
    plt.show()

# Example usage
points = [(0, 0), (2, 3), (4, 1)]
plot_triangle(points)