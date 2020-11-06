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

#Exercise 7.1 (Import and Examine)
jems = pd.read_csv('data/diamonds.csv')
jems

#Exercise 7.2 (Examine structure)
jems.info()

#Exercise 7.3 (Counting individual groups) 
# - How many diamonds with a clarity of category 
# “IF” are present in the data-set?
len(jems[(jems.clarity == "IF")])
jems_clrcnt=jems.clarity.value_counts()
# - What fraction of the total do they represent?
len(jems[(jems.clarity == "IF")])/len(jems)



#Exercise 7.4 (Summarizing proportions) 
# - What proportion of the whole is made up of each category of clarity?
jems['clarity'].value_counts()/len(jems)


#Exercise 7.5 (Find specific diamonds prices) 
# - What is the cheapest diamond price overall? 
jems['price'].min() # 326

# - What is the range of diamond prices? 
def getRange (x):
    low = min(x)
    high = max(x)
    return low, high
price_range = getRange(jems.price)
price_range
# - What is the average diamond price in each category of cut and color?
jems.groupby('cut')['price'].mean()
jems.groupby('color')['price'].mean()


#Exercise 7.6 (Basic plotting) 
# Make a scatter plot that shows the diamond price described by carat.
sns.scatterplot(x='carat',y='price',data=jems)

#Exercise 7.7 (Applying transformations) 
# Apply a log10 transformation to both the price and carat 
# store these as new columns in the DataFrame: price_log10 and carat_log10.

price_log10=np.log10(jems['price'])
price_log10
carat_log10=np.log10(jems['carat'])
carat_log10

jems_log10=pd.DataFrame({'price_log10': price_log10, 'carat_log10': carat_log10})
jems_log10

#Exercise 7.8 (Basic plotting) 
#Redraw the scatterplot using the transformed values.
sns.scatterplot(x='carat_log10',y='price_log10',data=jems_log10)

#Exercise 7.9 (Viewing models) 
# Define a linear model that describes the relatioship shown in the plot.
model = ols("price_log10 ~ carat_log10", jems_log10)
results = model.fit()
results.summary()

sns.lmplot(x='carat_log10',y='price_log10',data=jems_log10)

#Exercise 7.10 (Export data)
# Refer to the following table and save your data with transformed 
# values on your computer.
jems_log10.to_csv('data/jems_log10.csv')



