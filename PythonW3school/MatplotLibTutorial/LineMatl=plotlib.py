'''
Linestyle
You can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line:
'''
# use a dotted line
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, ms=10,  ls='dotted')

plt.show()
plt.plot(ypoints, ms=12,  ls='dashed')
plt.show()
# we can use the dotted as ':' and the dashed as '--'
'''
Line Color
You can use the keyword argument color or the shorter c to set the color of the line:
'''
plt.plot(ypoints,  color='r')

plt.show()

'''
Line Width
You can use the keyword argument linewidth or the shorter lw to change the width of the line.

The value is a floating number, in points:
'''

plt.plot(ypoints, ls='--', lw='20.5')
plt.show()

'''
Multiple Lines
You can plot as many lines as you like by simply adding more plt.plot() functions:
'''
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()
