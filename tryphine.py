import matplotlib.pyplot as plt
import numpy as np

# Define the coordinates
x_coords = [1, 2, 3, 4, 5]
y_coords = [2, 4, 5, 4, 6]

# Calculate the standard deviation
x_std_dev = np.std(x_coords)
y_std_dev = np.std(y_coords)

# Print the standard deviation
print("X-coordinate standard deviation:", x_std_dev)
print("Y-coordinate standard deviation:", y_std_dev)

# Plot the coordinates
plt.scatter(x_coords, y_coords)
plt.show()
