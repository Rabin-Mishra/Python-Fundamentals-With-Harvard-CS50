'''
Matplotlib Pie Charts
Creating Pie Charts
With Pyplot, you can use the pie() function to draw pie charts:
'''

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
plt.pie(y)
plt.show()
'''
As you can see the pie chart draws one piece (called a wedge) for each value in the array (in this case [35, 25, 25, 15]).

By default the plotting of the first wedge starts from the x-axis and moves counterclockwise:



Note: The size of each wedge is determined by comparing the value with all the other values, by using this formula:

The value divided by the sum of all values: x/sum(x)


'''
'''
Labels
Add labels to the pie chart with the labels parameter.

The labels parameter must be an array with one label for each wedge:
'''

y_axis = np.array([35, 25, 25, 15])
mylabels = ['Apples', 'Bananas', 'Cherries', 'Dates']

plt.pie(y, labels=mylabels)
plt.show()

# starting at a different angle for using the startangle argument in the pie function

plt.pie(y, labels=mylabels, startangle=90)
plt.show()

'''
Explode
Maybe you want one of the wedges to stand out? The explode parameter allows you to do that.

The explode parameter, if specified, and not None, must be an array with one value for each wedge.

Each value represents how far from the center each wedge is displayed:
'''
myexplode = [0.2, 0, 0, 0]
plt.pie(y, labels=mylabels, startangle=0, explode=myexplode)
plt.show()

# For adding the shadows to the pie chart set the shadow parameter to be TRUE
plt.pie(y, labels=mylabels, startangle=0, explode=myexplode, shadow=True)
plt.show()
