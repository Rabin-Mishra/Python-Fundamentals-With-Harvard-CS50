'''
Matplotlib Markers
Markers
You can use the keyword argument marker to emphasize each point with a specified marker:
'''
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])
# here since we handn't given any xpoints values so the x points will be automatically assigned as [0,1,2,3] equal to the number of coordinates of y axis

plt.plot(ypoints, marker='o')
plt.show()

plt.plot(ypoints, marker='*')
plt.show()

# code for different markers

# Define x and y data points
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

# Define marker styles
markers = ['o', '*', '.', ',', 'x', 'X', '+', 'P', 's', 'D', 'd',
           'p', 'H', 'h', 'v', '^', '<', '>', '1', '2', '3', '4', '|', '_']

# Plot each marker with corresponding data point
for i, marker in enumerate(markers[:len(x)]):
    plt.scatter(x[i], y[i], marker=marker, label=marker)

# Add legend
plt.legend(title='Marker', loc='upper right')

# Show plot
plt.show()
