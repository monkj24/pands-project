# Iris Data Set
# Author : Joanna Mnich

# 1: Analysis of data

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

# Calculate the mean of each variable
variable_means = df.mean(numeric_only=True) # numeric_only=True , tells pandas to calculate only column with numeric data types
print("Mean of each variable:")
print(variable_means)

# Calculate the minimum of each variable

variable_minimum = df.min(numeric_only=True)
print("Minimum of each variable:")
print(variable_minimum)

# Calculate the maximum of each variable

variable_maximum = df.max(numeric_only=True)
print("Maximum of each variable:")
print(variable_maximum)

# Calculate the standard deviation of each variable

variable_stdev = df.std(numeric_only=True)
print("Standard Deviation of each variable:")
print(variable_stdev)

# Calculate the median of each variable

variable_median = df.median(numeric_only=True)
print("Median of each variable:")
print(variable_median)

# B). Output summary statistics to summary.txt

with open('summary.txt', 'w') as f:         # open file summary.txt in write mode, and properly close using'with' statement after writing is finish
    f.write("Summary of Numerical Variables:\n\n")   # write header and add blank line
    for column in df.select_dtypes(include='float64').columns:   # Used loops through all columns to write statistics
        f.write(f"Column: {column}\n")
        f.write(f"  Mean: {df[column].mean():.2f}\n")  # write up to 2 decimal places
        f.write(f"  Median: {df[column].median():.2f}\n")
        f.write(f"  Std Dev: {df[column].std():.2f}\n")
        f.write(f"  Min: {df[column].min():.2f}\n")
        f.write(f"  Max: {df[column].max():.2f}\n")
        f.write(f"  Missing: {df[column].isna().sum()}\n\n") # counts missing value, detect early quality of data, and errors
    
    # Summary of categorical variable
    f.write("Summary of Categorical Variable:\n\n")  # code writes header about categorical column, add also blank line after
    f.write("Column: class\n")                       # class column na,e will be summerized
    f.write(f"  Unique Classes: {df['class'].nunique()}\n") # nunique counts the number of class categories
    f.write(f"  Classes: {df['class'].unique().tolist()}\n") # returns a NumPy array of unique values in the 'class' column, 
                                                            # tolist(). converts array to list
    f.write(f"  Class Counts:\n{df['class'].value_counts()}\n")  # counts and returns the series in each class


# 2: Generate and save histograms for each numerical variable

numeric_columns = df.select_dtypes(include='float64').columns   # numeric_columns is a list of all floats64 column names

for column in numeric_columns:   # used loop through each column
    plt.figure()
    plt.hist(df[column], bins=20, color='skyblue', edgecolor='black')   # plots histogram with special colour choosed, divided into 20 bins
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(True)    # to easy read value adds grid to plot
    plt.tight_layout()  # tidy up labels, title
    plt.savefig(f'{column}_hist.png')  # Histogram saved into files with seperate name of column () _hist.png
    plt.close()   # close figure and prevent interruption with the following plot

# 3: Scatter plots for each pair of numeric variables

import seaborn as sns

# Generate scatter plots for each pair of numeric variables
numeric_columns = df.select_dtypes(include='float64').columns

for i in range(len(numeric_columns)):
    for j in range(i+1, len(numeric_columns)):   # generates relationship between columns
        col1, col2 = numeric_columns[i], numeric_columns[j]  
        plt.figure(figsize=(6, 4))
        sns.scatterplot(data=df, x=col1, y=col2, hue='class', palette='viridis')  # use seaborn to plot
        plt.title(f'Scatter plot of {col1} vs {col2}')
        plt.xlabel(col1)
        plt.ylabel(col2)
        plt.legend(title='Class')
        plt.tight_layout()
        plt.savefig(f'{col1}_vs_{col2}.png')
        plt.close()


# 4: Box Plots by Class

# Create box plots for each numeric column by class

for column in numeric_columns:
    plt.figure(figsize=(6, 4))
    sns.boxplot(x='class', y=column, data=df, hue='class', palette='Set2', showfliers=False)
    plt.title(f'Boxplot of {column} by class')
    plt.tight_layout()
    plt.savefig(f'{column}_boxplot_by_class.png')
    plt.close()

# 5: Pairplot

sns.pairplot(df, hue='class', palette='coolwarm')
plt.savefig('pairplot.png')
plt.close()


