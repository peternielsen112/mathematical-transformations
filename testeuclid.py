import matplotlib.pyplot as plt

# Define the coordinates of the triangle vertices
x = [0, 1, 2]  # x-coordinates
y = [0, 1, 0]  # y-coordinates

# Plot the triangle
plt.plot(x, y, 'r-')  # 'r-' specifies red lines

# Fill the triangle (optional)
plt.fill(x, y, 'b', alpha=0.3)  # 'b' for blue, alpha for transparency

# Show the plot
plt.show()