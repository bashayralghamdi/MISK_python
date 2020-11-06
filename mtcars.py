# import an entire library
import math # Functions beyond the basic maths
# Import an entire library and give it an alias
import pandas as pd # For DataFrame and handling
import numpy as np # Array and numerical processing
import matplotlib.pyplot as plt # Low level plotting
import seaborn as sns # High level Plotting
import statsmodels.api as sm # Modeling, e.g. ANOVA

# Import only specific modules from a library
# we'll use this for the t-test function
from scipy import stats
# Import only specific functions from a library 
# ols is for ordinary least squares
from statsmodels.formula.api import ols


#Exercise 4.6 To get familiar with basic functions 
# and methods in Python data frames, try to solve 
# the following problems using the classic mtcars data set. 
# You can find this data set in your data directory.

#Import the data set and assign it to the variable mtcars.
mtcars =pd.read_csv('data/mtcars.csv')


#Calculate the correlation between mpg and wt and test if it is significant.
cor_mat = mtcars.corr()
cor_mat[['wt']].iloc[0]

#Visualize the relationship in an XY scatter plot.
plt.scatter(x='wt',y='mpg',data=mtcars)

#Convert weight from pounds to kg.
mtcars['wt_kg'] = mtcars['wt']/2.2046226218
mtcars





