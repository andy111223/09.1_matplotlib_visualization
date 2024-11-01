import pandas as pd
import numpy as np
import datetime as dt

# Creating a DataFrame
df = pd.DataFrame({
    'A': np.random.randn(200),
    'B': [dt.datetime(2019, 1, 1) + dt.timedelta(days=x) for x in range(200)],
    'C': np.arange(1, 201)
})

# Creating a histogram for column 'A'
df['A'].hist(bins=30)

# Creating a bar chart for the first 10 rows of column 'C'
df['C'].loc[:10].plot(kind='bar')

# Creating a line plot with custom size, color, and line width
df.plot.line(x='B', y='A', figsize=(12, 5), color='red', linewidth=2)