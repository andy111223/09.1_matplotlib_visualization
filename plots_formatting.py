import numpy as np
import matplotlib.pyplot as plt

# Adding a legend to a plot
x = np.arange(11)
fig, ax = plt.subplots()
ax.plot(x, x**2, label='x^2', color='blue', linewidth=2, linestyle='-')
ax.plot(x, x**3, label='x^3', color='red', linewidth=2, linestyle='--')
ax.legend(loc='best')
plt.show()

# Customizing lines and markers
fig, ax = plt.subplots()
ax.plot(x, x**2, label='x^2', color='red', linewidth=3, marker='o', markersize=10, markerfacecolor='orange')
ax.plot(x, x**3, label='x^3', linewidth=3, linestyle='-.', marker='*', markersize=10)
plt.show()

# Managing ticks and custom formatting
fig, ax = plt.subplots()

years = np.array(['2017', '2018', '2019', '2020F'])
revenues = [1.5e5, 2.5e6, 5.5e6, 2.0e7]

def million(x, pos):
    return f'PLN {x * 1e-6:.1f}M'

formatter = plt.FuncFormatter(million)
ax.yaxis.set_major_formatter(formatter)
ax.yaxis.set_major_locator(plt.MultipleLocator(5e6))

ax.bar(years, revenues)
ax.set_ylim(0, 8e6)
plt.show()