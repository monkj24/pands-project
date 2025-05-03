# Iris Data Set
# Author : Joanna Mnich

# 1: Analyze data

import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt


# Define column names based on the dataset structure
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'] 

# Read the data file 
df = pd.read_csv('iris_data/iris.data', names=column_names)  #function read CSV file into a Data Frame, use path to iris data set file

# Check the shape of the dataset
print("Shape of the dataset: ", df.shape) # shape shows information about structure of data (rows, columns)

# Preview the data
print(df.head(150))

# A) Math calculation

# Calculate the mean of each feature

variable_means = df.mean(numeric_only=True) # numeric_only=True , tells pandas to calculate only column with numeric data types
print("Mean of each variable:")
print(variable_means)

# Calculate the minimum of each feature

variable_minimum = df.min(numeric_only=True)
print("Minimum of each variable:")
print(variable_minimum)

# Calculate the maximum of each feature

variable_maximum = df.max(numeric_only=True)
print("Maximum of each variable:")
print(variable_maximum)

# Calculate the standard deviation of each feature

variable_stdev = df.std(numeric_only=True)
print("Standard Deviation of each variable:")
print(variable_stdev)

# Calculate the median of each feature

variable_median = df.median(numeric_only=True)
print("Median of each variable:")
print(variable_median)


# B.) Histogram


np.random.seed(1) 

normData = np.random.normal(size=10000)

plt.hist(normData)
plt.show()
'''