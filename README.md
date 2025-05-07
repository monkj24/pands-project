# Programming and Scripting

by Joanna Mnich

# 1. Introduction

This project is part of the Programming and Scripting coursework.
The objective is to apply programming techniques and basic machine learning methods to solve a real-world classification problem.
It covers fundamental concepts such as data collection, cleansing, visualization, and interpretation.
The project investigates statistical approaches, data collection methods, and fundamental machine learning algorithms for extracting useful information from data

# 2. Iris Data



The simplicity and structure of the Iris dataset made it an ideal starting point for understanding fundamental Programming and Scripting.

<img src="iris2.png" alt="Iris flower" width="300"/>

Photo by <a href="https://www.thespruce.com/irises-for-flower-garden-1315808/" rel="nofollow">Irises</a>.</p> 


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

One the section of mathematical calculation focuses on measures of mean, minimum, maximum, standard deviation, and median. I used the code from Pandas.pydata to determine those particular measurements. I specify that only numeric data should be included in the calculation by using the numeric_only=True parameter in the generated code. 
A summary of all calculations is included in the file summary.txt. With the help of AI  file summary includes data from the maths calculation from file analysis.py. The code separates the summary into numerical and categorical sections. All measurements with up to 2 decimal places are described using loop code. At the end is also used 'missing' to recognize early any error, missing value. 


### D) Histogram

In statistics, a histogram is a graphical representation of the distribution of numerical data. A histogram visualizes data distribution in time, highlighting trends and patterns.
The data frame was filtered to include only column names and data type float64. The float64 is a large bit of memory, used when precision matters mostly in scientific calculations. Allows concentrating on floating-point numbers, numbers with decimal places, and showing data to 17th decimal places. 
To create histogram I used loop function 

### E) Scatter plots

### F) Box plots

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



