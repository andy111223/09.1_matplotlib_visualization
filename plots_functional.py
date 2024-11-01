# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Jupyter Notebook only
# %matplotlib inline

# Create data
x = np.arange(11)
y = x ** 2

# Functional approach - basic line plot
plt.plot(x, y)
plt.show()

# Customize the plot
plt.plot(x, y, color='red', label='y = x^2')
plt.plot(x, y - 10, color='blue', linestyle='dashed', label='y = x^2 - 10')
plt.xlabel('X axis', size=15, color='indigo')
plt.ylabel('Y axis', size=15, color='indigo')
plt.title('Line Plot Example', size=20, color='navy')
plt.xticks(color='indigo')
plt.yticks(color='indigo')
plt.grid()
plt.axhline(y=50, color='k', linestyle='--')
plt.axvline(x=5, color='k', linestyle='--')
plt.legend()
plt.show()

# Subplots
plt.subplot(1, 2, 1)
plt.plot(x, y, color='red')

plt.subplot(1, 2, 2)
plt.plot(y, x, color='blue')
plt.show()

# Koch snowflake
def koch_snowflake(order, scale=10):
    def _koch_snowflake_complex(order):
        if order == 0:
            angles = np.array([0, 120, 240]) + 90
            return scale / np.sqrt(3) * np.exp(np.deg2rad(angles) * 1j)
        else:
            ZR = 0.5 - 0.5j * np.sqrt(3) / 3
            p1 = _koch_snowflake_complex(order - 1)
            p2 = np.roll(p1, shift=-1)
            dp = p2 - p1
            new_points = np.empty(len(p1) * 4, dtype=np.complex128)
            new_points[::4] = p1
            new_points[1::4] = p1 + dp / 3
            new_points[2::4] = p1 + dp * ZR
            new_points[3::4] = p1 + dp / 3 * 2
            return new_points
    points = _koch_snowflake_complex(order)
    x, y = points.real, points.imag
    return x, y

x, y = koch_snowflake(order=5)
plt.fill(x, y)
plt.axis('equal')
plt.show()

# Scatter plot example
rand_arr = np.random.randint(1, 1000, 2000).reshape(1000, 2)
plt.figure(figsize=(10, 5))
plt.scatter(rand_arr[:, 0], rand_arr[:, 1], c='blue')
plt.show()
