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

IDE helps write, run, and debug the code. Code loads data, calculates, creates plots, and diagrams. 
Code in Python can:
- Perform calculations from loaded data, like means, standard deviation, and median.
- Analyse data from libraries: pandas, numpy, seaborn, matplotlib
- Create machine learning model: scikit-learn
- Controls files and folders by creating automated scripts

### B) Iris data 

The Iris dataset was loaded as a zip file using url from the UC Irvine Machine Learning Repository archive to my desktop file
   https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
After downloading zip file was extracted before loading into the repository
In my repository, using code to read data, df = pd.read_csv, the Function returns the iris data.


