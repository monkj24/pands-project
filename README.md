# Programming and Scripting

by Joanna Mnich

# 1. Introduction

This project is part of the Programming and Scripting coursework.
The objective is to apply programming techniques and basic machine learning methods to solve a real-world classification problem.
It covers fundamental concepts such as data collection, cleansing, visualization, and interpretation.
The project investigates statistical approaches, data collection methods, and fundamental machine learning algorithms for extracting useful information from data

# 2. Iris Data



The simplicity and structure of the Iris dataset made it an ideal starting point for understanding fundamental Programming and Scripting.

<img src="iris_picture.png" alt="Iris flower" width="300"/>

Photo by <a href="https://www.thespruce.com/irises-for-flower-garden-1315808/" rel="nofollow">Iris</a>.</p> 


# 3. Steps of creating a project

### A) How to run Python code

- To run the Python code, first, it is necessary to download the Python program from Python.org onto the computer (recommended new version 3.7)
- Open VS Code IDE, write a file with the extension .py, and run it
- In the file, write some code 
- Open a new terminal and check the code to see if it's working. Write in your file path: python ./file.py

The IDE helps write, run, and debug the code. The code loads data, calculates, and creates plots and diagrams. 
Code in Python can:
- Calculate the loaded data's means, standard deviation, and median.
- Analyse data from libraries: pandas, numpy, seaborn, matplotlib
- Create machine learning model: scikit-learn
- Controls files and folders by creating automated scripts

### B) Iris data 

The Iris dataset was loaded as a zip file using the URL from the UC Irvine Machine Learning Repository archive to my desktop file
   https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
After downloading, the zip file was extracted before loading it into the repository
In my repository, using code to read data, df = pd.read_csv, the Function returns the iris data.

### C) Analysis of Data

In this section, I first imported the necessary module (math) and libraries (pandas, matplotlib, pyplot, and numpy).
Pandas library is like a spreadsheet, using DataFrames, to read and write files, filter, and group data.
The Matplotlib.pyplot library helps make plots, histograms, and scatterplots.
The Numpy library efficiently works with arrays, matrices, and mathematical functions.
The math module makes basic mathematical function calculations.

In the next step, I defined column names, and added to the end also the class. Column names are written in order as in the data.
Data is downloaded to the file iris_data/iris.data. Used code df = pd.read_csv(), I read the iris.data to the repository.
In an analysis of the data, I start by defining the shape of the dataset. The shape shows information about the structure of data(rows, columns). I used the function df - define.
In print, I have a little problem, because using print(df.head), the output shows me only the first 5 lines. After research, I decided to add in a separate bracket 150, to print, show me all rows, but with a break in the middle.

The section of mathematical calculation focuses on measures of mean, minimum, maximum, standard deviation, and median. I used the code from Pandas.pydata to determine those particular measurements. I specify that only numeric data should be included in the calculation by using the numeric_only=True parameter in the generated code. 
A summary of all calculations is included in the file summary.txt. With the help of AI  file summary includes data from the maths calculation from file analysis.py. The code separates the summary into numerical and categorical sections. All measurements with up to 2 decimal places are described using loop code. At the end is also used 'missing' to recognize early any error, missing value. 


### D) Histogram

In statistics, a histogram is a graphical representation of the distribution of numerical data. A histogram visualizes data distribution in time, highlighting trends and patterns.
The data frame was filtered to include only column names and data type float64. The float64 is a large bit of memory, used when precision matters mostly in scientific calculations. Allows concentrating on floating-point numbers, numbers with decimal places, and showing data to 17th decimal places. 
To create a histogram, I used a loop function, which, by running through every column, creates different histograms. The code plt.figure(). creates a fresh, separate histogram from the data; without this, the plots might cross or be drawn on the same figure. Plotted histograms describe the count of bins, special colours, titles, and labels.
The grids are adding to the plot for easy reading of values. The function plt.tight_layout() tidies up labels and title to be clearly visible. 
At the end, histograms are saved in files named after the column name with the extension .png.

### E) Scatter plots

A scatter plot is a mathematical tool used to display data and show the relationship between two variables.  It is typically used to plot the relationship between one independent and one dependent variable. Each dot's position on the horizontal and vertical axes represents a single data point's value.
Here, I use the seaborn library to more easily produce a scatter plot and create styling and color. Like in the histogram, the same function is used to filter data to include only column names with data type float64. Double 'for' used in a function must generate a relationship between column names, for example (sepal_length vs sepal_width), but avoid relationships of opposite (sepal_width vs sepal_length), and relationships of the same names (sepal_length vs sepal_length).
I asked AI to explain the relationship between columns in code col1, col2 =().  The table below describes those connections to better understand:
| `i` | `j` | `col1`          | `col2`          |
| --- | --- | --------------- | --------------- |
| 0   | 1   | 'sepal\_length' | 'sepal\_width'  |
| 0   | 2   | 'sepal\_length' | 'petal\_length' |
| 0   | 3   | 'sepal\_length' | 'petal\_width'  |
| 1   | 2   | 'sepal\_width'  | 'petal\_length' |
| 1   | 3   | 'sepal\_width'  | 'petal\_width'  |
| 2   | 3   | 'petal\_length' | 'petal\_width'  |

The seaborn function sns.scatterplot() is used to plot one variable against another, separated by class color (hue='class), and type gradient (palette='viridis').
A legend, a title, and labels with overlap prevention were added to the plot. At the end, plots were saved as PNG files named after the two columns.

### F) Box plots

A box plot is a graph that displays the distribution of a dataset. It presents essential summary statistics such as the median, quartiles, and expected outliers in a clear and graphic format. Box plots allow  to present an overview of the distribution, highlight potential, and examine different datasets in a simple and visual format.

To create a boxplot, I used the loop function to visualize how variables are distributed using quartiles. Function creates one separate boxplot for each class. All boxplots are saved as image files.

### G) Pairplot



# 4. References

4.1 Analysis of data

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html

https://pandas.pydata.org/pandas-docs/stable/reference/frame.html

4.2 Summary file

https://chatgpt.com/c/6819f351-f14c-800b-b3d1-b2ddc1bd1965        # basic help to summary file

https://docs.python.org/3/library/functions.html#open              # open for wtiting

https://docs.python.org/3/reference/compound_stmts.html#with       # statement 'with' to close when finished

https://docs.python.org/3/library/io.html#io.TextIOBase.write      # f.write function

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.select_dtypes.html   # df.select_dtypes 

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.nunique.html     

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.unique.html

https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tolist.html

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html

4.3 Histogram

https://stackoverflow.com/questions/43440821/the-real-difference-between-float32-and-float64   # float64 explanation

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.select_dtypes.html  # Dataframe,df.type with float64

https://docs.python.org/3/tutorial/controlflow.html#for-statements   # loop statements

https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html   # plotting figure

https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html   # draws a histogram

https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html   # add title, labels

https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html    # add grid

https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html  # to not overlap, add tight layout

https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html   # saving histogram to file

4.4 Scatter Plot

https://www.geeksforgeeks.org/scatter-plot/    # What is a scatter plot

https://chatgpt.com/c/681dc425-2774-800b-8247-00a5db63ac3a   # explanation of relationship between columns 

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.select_dtypes.html   # df.type with float64

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.columns.html   # returns the column labels from DataFrame

https://docs.python.org/3/tutorial/controlflow.html#for-statements # loop function with range(len)

https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html    # plt.figure

https://matplotlib.org/stable/users/explain/customizing.html#matplotlibrc-sample   # figsize(6,4)

https://seaborn.pydata.org/generated/seaborn.scatterplot.html  # seaborn scatter plot

https://matplotlib.org/stable/api/pyplot_summary.html # description of scatter plot with saving to a PNG file

4.5 Boxplot

https://www.geeksforgeeks.org/box-plot/  # What is a boxplot

https://docs.python.org/3/tutorial/controlflow.html#for-statements   # for loop function

https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html   # plt.figure

https://seaborn.pydata.org/generated/seaborn.boxplot.html  # seaborn boxplot

https://matplotlib.org/stable/api/pyplot_summary.html  # description of boxplot with saving to a PNG file

4.6  Pairplot









