'''
Matplotlib Labels and Title
Create Labels for a Plot
With Pyplot, you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis.
also you can use title() for creating the title for the plot
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y, lw=2, color='r')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.title("Sports Watch")

plt.show()

'''
Set Font Properties for Title and Labels
You can use the fontdict parameter in xlabel(), ylabel(), and title() to set font properties for the title and labels.
'''
# Set font properties for the title and labels:
font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'red', 'size': 10}

plt.title("Sports Watch Data", fontdict=font1, loc='right')
plt.xlabel("Average Pulse", fontdict=font2)
plt.ylabel("Calorie Burnage", fontdict=font2)
plt.plot(x, y)
plt.show()
'''
Position the Title
You can use the loc parameter in title() to position the title.

Legal values are: 'left', 'right', and 'center'. Default value is 'center'.
'''
