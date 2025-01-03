'''
Colors
You can set the color of each wedge with the colors parameter.

The colors parameter, if specified, must be an array with one value for each wedge:
'''
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ['Apples', 'Bananas', 'Cherries', 'Dates']
mycolors = ['Red', 'Yellow', 'crimson', 'brown']
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels=mylabels, colors=mycolors, explode=myexplode, shadow=True)
plt.legend(title='Fruit Names')
plt.show()
