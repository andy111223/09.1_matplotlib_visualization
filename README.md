# Data Visualization with Matplotlib and Pandas
This repository contains scripts and Jupyter notebooks created for self-learning purposes, demonstrating various approaches to data visualization using Python. The work here primarily focuses on learning how to use Matplotlib and Pandas for data visualization. The content is divided into different sections based on the approaches to creating visualizations, with each section detailing the concepts, types of plots, and specific functions used.

## Functional Approach
The functional approach to plotting involves using individual functions to directly plot graphs, label axes, and customize visual elements.

### Concepts Learned:
- Functional plotting using plt functions.
- Basic customization (e.g., setting colors, labels, and titles).
- Adding multiple lines to a single plot.
### Library: Matplotlib.
### Functions Used:
- plt.plot()
- plt.xlabel(), plt.ylabel()
- plt.title()
- plt.xticks(), plt.yticks()
- plt.grid()
- plt.axhline(), plt.axvline()
- plt.subplot()
- plt.show()
### Types of Plots:
- Line plots
- Multiple subplots in a grid format

## Object-Oriented Approach
The object-oriented approach involves creating figure and axis objects and then manipulating them to build plots. This approach provides more flexibility and control over individual components.

### Concepts Learned: 
- Creating Figure and Axes objects.
- Adding axes to figures.
- Customizing individual subplots.
### Library: Matplotlib.
### Functions Used:
- plt.figure()
- fig.add_axes()
- axes.plot()
- axes.set_xlabel(), axes.set_ylabel(), axes.set_title()
- plt.subplots()
### Types of Plots:
- Line plots
- Custom subplots with different sizes and locations

## Plot Customization
Focused on personalizing plots by customizing colors, styles, markers, and axes properties.

### Concepts Learned:
- Setting line styles, colors, markers, and transparency (alpha).
- Adding legends with positioning options.
- Removing or formatting axis ticks and labels.
- Handling overlapping labels using MaxNLocator.
### Library: Matplotlib.
### Functions Used:
- axes.legend()
- axes.plot() with parameters like color, linestyle, marker, linewidth, etc.
- axes.yaxis.set_major_locator(), plt.MaxNLocator()
- plt.FuncFormatter(), plt.MultipleLocator()
- ax.set_ylim()
### Types of Plots:
- Line plots
- Bar plots with formatted axes

## Special Shapes and Advanced Customization
Leveraged advanced Matplotlib capabilities for creating more complex visualizations like Koch snowflake and multiple overlapping transparent shapes.

### Concepts Learned:
- Using functions to create custom shapes.
- Using transparency (alpha) for overlapping shapes.
### Library: Matplotlib.
### Functions Used:
- Custom functions like koch_snowflake()
- plt.fill()
- plt.axis()

## Scatter Plots and Pie Charts
Explored creating scatter plots and pie charts, emphasizing size and color customization.

### Concepts Learned:
- Creating scatter plots with different colors for different point conditions.
- Using figure() for resizing plots.
- Creating pie charts with labels and percentage representation.
### Library: Matplotlib, NumPy.
### Functions Used:
- plt.scatter()
- plt.figure()
- plt.pie()

## Pandas Built-in Visualization
Learned how to use Pandas’ built-in visualization capabilities, which are built on Matplotlib, for quick and easy visualizations.

### Concepts Learned:
Using Pandas’ .plot() function to generate different types of plots.
### Library: Pandas
### Functions Used:
- df.hist()
- df.plot(kind='bar')
- df.plot.line()
### Types of Plots:
- Histogram
- Bar chart
- Line plot

## Key Concepts Learned
- Matplotlib Basics: Functional and object-oriented approaches for plotting.
- Customizing Plots: Colors, markers, line styles, gridlines, legends, tick formatting, and labels.
- Advanced Custom Shapes: Custom functions for creating complex shapes like Koch snowflakes.
- Scatter and Pie Charts: Creating and customizing scatter plots and pie charts.
- Handling Subplots: Creating independent subplots and working with figure grids.
- Pandas Visualization: Using Pandas for simple and fast visualizations.
- CRISP-DM: Applied the CRISP-DM (Cross-Industry Standard Process for Data Mining) approach as part of data visualization and feature engineering in data exploration.

## Libraries
- Matplotlib: Core library for creating visualizations.
- Pandas: Used for data manipulation and integrated visualizations.
- NumPy: Used for generating numerical data used in plots.

## Clone the Repository

`git clone https://github.com/andy111223/09.1_matplotlib_visualization.git`
