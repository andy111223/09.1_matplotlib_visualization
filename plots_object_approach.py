import numpy as np
import matplotlib.pyplot as plt

# Object-Oriented Approach

# Create a figure (blank canvas)
fig = plt.figure()

# Add axes to the figure
axes = fig.add_axes([0, 0, 1, 1])  # left, bottom, width, height

# Data to plot
x = np.arange(11)
y = x ** 2

# Plot on the axes
axes.plot(x, y)
axes.set_xlabel('oś X')  # Label for X-axis
axes.set_ylabel('oś Y')  # Label for Y-axis
axes.set_title('Tytuł wykresu')  # Title of the plot

plt.show()

# Adding multiple sets of axes
fig = plt.figure()
axes1 = fig.add_axes([0, 0, 1, 1])  # Larger axes
axes2 = fig.add_axes([0.2, 0.2, 0.8, 0.8])  # Smaller inset axes

# Plot data on each axis
axes1.plot(x, y)
axes2.scatter(np.random.randint(0, 11, 11), np.random.randint(0, 121, 11))

axes1.set_xlabel('Exponential')
axes2.set_xlabel('Random')

plt.show()

# Using subplots to create multiple axes at once
fig, axes = plt.subplots(nrows=1, ncols=2)

# Plot different data on each subplot
axes[0].plot(x, y)
axes[1].plot(y, x)

plt.show()