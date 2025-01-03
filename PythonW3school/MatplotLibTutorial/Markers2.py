'''
Format Strings fmt
You can also use the shortcut string notation parameter to specify the marker.

This parameter is also called fmt, and is written with this syntax:

marker|line|color
'''
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, 'o:r')  # in place of : we can use '-','__','-.'
plt.show()

'''
Marker Size
You can use the keyword argument markersize or the shorter version, ms to set the size of the markers:
'''
plt.plot(ypoints, marker='o', ms=20)
plt.show()

'''
Marker Color
You can use the keyword argument markeredgecolor or the shorter mec to set the color of the edge of the markers:
'''

plt.plot(ypoints, marker='o', ms=20, mec='r')
plt.show()
'''
You can use the keyword argument markerfacecolor or the shorter mfc to set the color inside the edge of the markers:
'''
plt.plot(ypoints, marker='o', ms=20, mec='r', mfc='g')
plt.show()
