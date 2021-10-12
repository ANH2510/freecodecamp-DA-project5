import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    df.plot.scatter('Year', 'CSIRO Adjusted Sea Level', figsize = (10,10))


    # Create first line of best fit
    yearto2051 = pd.Series(i for i in range(1980, 2051))
    slope, intercept, r_val, p_val, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(yearto2051, slope * yearto2051 + intercept,'r', label = 'best fit')


    # Create second line of best fit
    recent = df[df['Year'] >= 2000]
    yearto2051_n = pd.Series(i for i in range(2000, 2051))
    slope_n, intercept_n, r_val_n, p_val_n, std_err_n = linregress(recent['Year'], recent['CSIRO Adjusted Sea Level'])
    plt.plot(yearto2051_n, slope_n * yearto2051_n + intercept_n,'g', label = '>=2000')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches')
    plt.title('Rise in Sea level')
    plt.legend(fontsize='medium')
    plt.show()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()