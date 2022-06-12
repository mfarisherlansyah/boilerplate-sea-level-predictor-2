import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv("epa-sea-level.csv")

    x_1 = data['Year'].to_numpy()
    y_1 = data['CSIRO Adjusted Sea Level'].to_numpy()

    (slope_1, intercept_1, rvalue_1, pvalue_1, stderr_1) = linregress(x_1, y_1)

    # Create scatter plot
    fig, ax = plt.subplots(figsize = (10, 8))

    ax.scatter(x_1, y_1, color = 'orange', label = 'Original Data')

    # Create first line of best fit
    x_reg_1 = np.arange(data["Year"][0], 2051)
    y_pred_1 = intercept_1 + slope_1 * x_reg_1
    ax.plot(x_reg_1, y_pred_1, color="green", label="Fitted line 1")

    # Create second line of best fit
    x_2 = data[data["Year"] >= 2000]["Year"].to_numpy()
    y_2 = np.round_(data[data["Year"] >= 2000]["CSIRO Adjusted Sea Level"].to_numpy(), 7)

    (slope_2, intercept_2, rvalue_2, pvalue_2, stderr_2) = linregress(x_2, y_2)

    x_reg_2 = np.arange(2000, 2051)
    y_pred_2 = intercept_2 + slope_2 * x_reg_2
    ax.plot(x_reg_2, y_pred_2, color="crimson", label="Fitted line 2")

    # Add labels and title
    plt.plot()
    # Set labels
    ax.legend(loc='best')
    ax.set_xlabel('Year') 
    ax.set_ylabel('Sea Level (inches)') 
    ax.set_title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()