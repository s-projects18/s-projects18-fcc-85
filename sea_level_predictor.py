import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

import numpy as np


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv", index_col="Year")
    # 'CSIRO Adjusted Sea Level', 'Lower Error Bound',
    # 'Upper Error Bound', 'NOAA Adjusted Sea Level'

    # Use matplotlib to create a scatter plot using the "Year" column as the x-axis and the "CSIRO Adjusted Sea Level" column as the y-axix
    plt.xlim(1850, 2075)
    plt.plot(df.index, df['CSIRO Adjusted Sea Level'], 'o', label='original data')

    # Create first line of best fit
    # Use the linregress function from scipi.stats
    # to get the slope and y-intercept of the line of best fit.
    # Plot the line of best fit over the top of the scatter plot.
    # Make the line go through the year 2050 to predict the sea level rise in 2050.
    # https://realpython.com/linear-regression-in-python/
    slope, intercept, r_value, p_value, std_err = linregress(df.index, df['CSIRO Adjusted Sea Level'])

    #x = df.index
    x = pd.Series(np.arange(1850,2076))
    plt.plot(x, intercept + slope*x, 'r', label='fitted line')

    # Create second line of best fit
    # Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset.
    # Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000
    df2000 = df.loc[df.index >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df2000.index, df2000['CSIRO Adjusted Sea Level'])

    x2 = pd.Series(np.arange(2000,2076))
    plt.plot(x2, intercept2 + slope2*x2, 'g', label='fitted line 2000')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    #plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()