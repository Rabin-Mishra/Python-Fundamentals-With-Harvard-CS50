'''
Matplotlib Bars
Creating Bars
With Pyplot, you can use the bar() function to draw bar graphs:
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.array(['A', 'B', 'C', 'D'])
y = np.array([3, 5, 8, 9])

plt.bar(x, y)
plt.show()

'''
Horizontal Bars
If you want the bars to be displayed horizontally instead of vertically, use the barh() function:
'''

# for horizontal bars
x_axis = np.array(['A', 'B', 'C', 'D'])
y_axis = np.array([3, 5, 8, 9])

plt.barh(x_axis, y_axis)

plt.show()

# for setting the color of the bar use the color argument to set the color of the bars

plt.bar(x, y, color='r')
plt.show()

# for setting the width of the bar
plt.bar(x, y, color='green', width=0.5)
plt.show()
