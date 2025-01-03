'''
Matplotlib Subplot
Display Multiple Plots
With the subplot() function you can draw multiple plots in one figure:
'''
# draw 2 plots

import numpy as np
import matplotlib.pyplot as plt

# plot1
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("Sales")

# plot 2
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.title("Income")
# Super Title
# You can add a title to the entire figure with the suptitle() function:
plt.suptitle("MY SHOP")
plt.show()
'''
The subplot() Function
The subplot() function takes three arguments that describes the layout of the figure.

The layout is organized in rows and columns, which are represented by the first and second argument.

The third argument represents the index of the current plot.

plt.subplot(1, 2, 1)
#the figure has 1 row, 2 columns, and this plot is the first plot.

plt.subplot(1, 2, 2)
#the figure has 1 row, 2 columns, and this plot is the second plot.
So, if we want a figure with 2 rows an 1 column (meaning that the two plots will be displayed on top of each other instead of side-by-side), we can write the syntax like this as plt.subplot(2,1,1) and plt.plot(2,1,2) so a single col and 2 rows for 2 figures being vertically aligned above one another
'''
# generate 6 plots
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 1)
plt.plot(y)
plt.title("Figure 1")

y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 2)
plt.plot(y)
plt.title("Figure 2")

y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 3)
plt.plot(y)
plt.title("Figure 3")

y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 4)
plt.plot(y)
plt.title("Figure 4")

y = np.array([1, 2, 3, 4])
plt.subplot(2, 3, 5)
plt.plot(y)
plt.title("Figure 5")

y = np.array([5, 6, 7, 8])
plt.subplot(2, 3, 6)
plt.plot(y)
plt.title("Figure 6")

plt.suptitle("Using subplot() to show 6 different graphs at the same time")
plt.show()
