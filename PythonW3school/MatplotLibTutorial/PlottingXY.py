'''
Matplotlib Plotting
Plotting x and y points
The plot() function is used to draw points (markers) in a diagram.

By default, the plot() function draws a line from point to point.

The function takes parameters for specifying points in the diagram.

Parameter 1 is an array containing the points on the x-axis.

Parameter 2 is an array containing the points on the y-axis.

If we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays [1, 8] and [3, 10] to the plot function.
'''
# Draw a line in a diagram from position (1, 3) to position (8, 10):
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()
'''
Plotting Without Line
To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.
'''
# Draw two points in the diagram, one at position (1, 3) and one in position (8, 10):
plt.plot(xpoints, ypoints, 'o')
plt.show()

# Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):

xcoord = np.array([1, 2, 6, 8])
ycoord = np.array([3, 8, 1, 10])

plt.plot(xcoord, ycoord)
plt.show()

# showing just the dots or points
plt.plot(xcoord, ycoord, 'o')
plt.show()
