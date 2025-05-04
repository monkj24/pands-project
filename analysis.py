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

# B). Output summary statistics to summary.txt

with open('summary.txt', 'w') as f:
    f.write("Summary of Numerical Variables:\n\n")
    for column in df.select_dtypes(include='float64').columns:
        f.write(f"Column: {column}\n")
        f.write(f"  Mean: {df[column].mean():.2f}\n")
        f.write(f"  Median: {df[column].median():.2f}\n")
        f.write(f"  Std Dev: {df[column].std():.2f}\n")
        f.write(f"  Min: {df[column].min():.2f}\n")
        f.write(f"  Max: {df[column].max():.2f}\n")
        f.write(f"  Missing: {df[column].isna().sum()}\n\n")
    
    # Summary of categorical variable
    f.write("Summary of Categorical Variable:\n\n")
    f.write("Column: class\n")
    f.write(f"  Unique Classes: {df['class'].nunique()}\n")
    f.write(f"  Classes: {df['class'].unique().tolist()}\n")
    f.write(f"  Class Counts:\n{df['class'].value_counts()}\n")


# B.) Histogram for each variable

import numpy as np
import matplotlib.pyplot as plt

# Parameters for the normal distribution
mean = 5
std_dev = 2
num_samples = 1000

np.random.seed(1)
normData = np.random.normal(mean, std_dev, num_samples)

# the figure and primary axis
fig, ax1 = plt.subplots()


# Plot the histogram of the normal distribution

ax1.hist(normData, bins=30, density=True, alpha=0.5, color='blue', label='Normal Distribution (µ=5, σ=2)')
ax1.set_ylabel('Density', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')



plt.hist(normData)
plt.show()
'''