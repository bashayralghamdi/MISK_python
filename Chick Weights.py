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
from statsmodels.stats.multicomp import (pairwise_tukeyhsd,MultiComparison)


#Exercise 2.1 In the data folder you’ll find another file called “Chick Weights.txt.”
#Import the data set and assign it to the variable chickwts.
chickwts =pd.read_table('data/Chick Weights.txt')

chickwts.columns

# Calculate the mean and standard deviation for each group.
# mean and standard for all
chickwts.describe()
chickwts['weight'].mean()
chickwts['weight']
chickwts['weight'].std()
# mean for each group
chickwts.groupby(['feed']).mean()
chickwts.groupby('feed')['weight'].mean()
chickwts.groupby('feed')[['weight']].mean()
#standard deviation for each group
chickwts.groupby(['feed']).std()
chickwts.groupby('feed')['weight'].std()
chickwts.groupby('feed')[['weight']].std()

#Calculate the number of chicks in each group.
chickwts['feed'].value_counts()

#Calculate a within-group z-score.
stats.zscore(chickwts['weight'])

#Produce a strip chart showing each chick as an
#individual data point
sns.stripplot(y='weight',x='feed',data=chickwts)

#Calculate a 1-way ANOVA.
model = ols("weight ~ feed", chickwts)
results = model.fit()
aov_table = sm.stats.anova_lm(results, typ=2)
aov_table

#Calculate Tukey’s post-hoc test (i.e. p-values for all
#  pair-wise t-tests)

MultiComp = MultiComparison(chickwts['weight'],chickwts['feed'])
MultiComp.tukeyhsd().summary()

