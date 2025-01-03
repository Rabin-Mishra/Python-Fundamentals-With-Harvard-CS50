'''
Matplotlib Histograms
Histogram
A histogram is a graph showing frequency distributions.

It is a graph showing the number of observations within each given interval.

Example: Say you ask for the height of 250 people, you might end up with a histogram like this:
'''
'''
Create Histogram
In Matplotlib, we use the hist() function to create histograms.

The hist() function will use an array of numbers to create a histogram, the array is sent into the function as an argument.

For simplicity we use NumPy to randomly generate an array with 250 values, where the values will concentrate around 170, and the standard deviation is 10
'''
import numpy as np
import matplotlib.pyplot as plt
x = np.random.normal(170, 10, 250)
print(x)
plt.hist(x)
plt.show()
