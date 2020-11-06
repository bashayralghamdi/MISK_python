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

#Exercise 3.5 Using what we’ve seen in the Plant Growth
# case study:
#Import the data set and assign it to the variable mtcars.
plant_growth = pd.read_csv('data/plant_growth.csv')

len(plant_growth['weight'])	#The number of values, n
np.mean(plant_growth['weight'])	#The mean
np.median(plant_growth['weight'])	#The median
np.var(plant_growth['weight'])	#The variance
np.std(plant_growth['weight'])	#The standard deviation
stats.iqr(plant_growth['weight'])	#The inter-quartile range
max(plant_growth['weight'])	#The maximum value
min(plant_growth['weight'])	#The minimum value

#Exercise 9.1 Get a unique list of values in the 
# group column of plant_growth.
treatment_groups=plant_growth.group.unique()

for value in treatment_groups:
    result=np.mean(plant_growth.weight[plant_growth.group == value])
    print(f"the mean of {value} is {result}")

