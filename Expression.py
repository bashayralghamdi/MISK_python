
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

#Exercise 8.2 (Import data) Import Expression.txt. 
#Save it as an object called medi.
#Import the data set and assign it to the variable mtcars.
medi =pd.read_table('data/Expression.txt')
medi
#Exercise 8.3 (Tidy data) Convert the data set to a tidy format.
medi_melt = pd.melt(medi)
medi_melt
#create new columns that have spreated variable
medi_melt['treatment'], medi_melt['gene'], medi_melt['time'] = medi_melt['variable'].str.split('_').str
#delete unwanted column
medi_melt = medi_melt.drop('variable', axis=1)


#Exercise 8.4 (Calculate Statistics) Calculate each of the
# following statistics for each of the unique 24 combinations of gene,
# treatment and time:
#average the mean of the value
np.mean(medi_melt['value'])
medi_stat=medi_melt.groupby(['gene','treatment','time']).mean()
medi_stat
#n the number of observations in each group
medi_stat['n']=medi_melt.groupby(['gene','treatment','time']).count()

#SEM The standard error of the mean
medi_stat['SEM']=medi_stat['value']/np.sqrt(medi_stat['n'])

#CIerror The 95% CI error defined by the t distribution
#lower95 The upper 95% CI limit
medi_stat['CI_lower']=medi_stat['value'] - (1.96 *medi_stat['SEM'])/np.sqrt(medi_stat['n'])

#upper95 The upper 95% CI limit
medi_stat['CI_upper']=medi_stat['value'] + (1.96 *medi_stat['SEM'])/np.sqrt(medi_stat['n'])

#Exercise 8.5 (Export data) Now that you’ve processed your data,
# refer to the following table and save a file on your computer 
# that contains the summary statistics.
medi_stat.to_csv('data/medi_stat.csv')









