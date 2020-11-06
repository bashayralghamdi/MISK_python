
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

#test vscode
plt.plot([1,23,2,4])
plt.ylabel('some numbers')


#Exercise 3.1 (Differences in handling types) What do expect
#  when executing the following functions?
1 + 1 #2

'1' + '1' #11

'1' * 5 #11111

'1' '1' #11



#Exercise 3.2 (Mixing different lengths) The first exercise was
# pretty easy… what would happen in these cases? Try to 
# predict the answer without executing code!

[1, 6, 9, 36] + 100 #TypeError: can only concatenate list (not "int") to list

[1, 6, 9, 36] + [10, 100] #[1, 6, 9, 36, 10, 100]

[1, 6, 9, 36] + [100, 200, 300, 400] #[1, 6, 9, 36, 100, 200, 300, 400]

[1, 6, 9, 36] + [100, "dogs", 300, 400] #[1, 6, 9, 36, 100, 'dogs', 300, 400]


#Exercise 3.3 (Functions and math) Given the definition
# of the Normal 95% confidence interval

heights = [167, 188, 178, 194, 171, 169]
height_mean=np.mean(heights)
height_stdv=np.std(heights)
height_len=len(heights)

CI_lower=height_mean - 1.96 *height_stdv/math.sqrt(height_len)
CI_upper=height_mean + 1.96 *height_stdv/math.sqrt(height_len)


#Exercise 3.4 Given the dist list for some cities:
cities = ['Munich', 'Paris', 'Amsterdam', 'Madrid', 'Istanbul']
dist = [584, 1054, 653, 2301, 2191]
#How many data points are there?
len(dist)#5	
#What is the longest and shortest distance?
max(dist)#2301
min(dist)#584
#Get the average distance
np.mean(dist)#1356.6
#Visualize the values in the dist list as a univariate 
# histogram
sns.histplot(dist)



#Exercise 3.6 (Creating functions) and ..
#Exercise 3.7 (Returning tuples)create a function that 
# takes a list and returns the lower limit and upper limit.
fun=confInt(heights)
def confInt(CIList):

    """ lower and upper limit of
     95% confidence interval  """

    list_mean=np.mean(CIList)
    list_stdv=np.std(CIList)
    list_len=len(CIList)
    
    CI_lower=list_mean - 1.96 *list_stdv/math.sqrt(list_len)
    CI_upper=list_mean + 1.96 *list_stdv/math.sqrt(list_len)
    
    return CI_lower,CI_upper


#Exercise 3.8 (Inner functions) Returning to confInt, 
#create a function within this function which manually calculates
confInt(heights)
def  confInt(CIList):   

    list_mean=np.mean(CIList)
    list_stdv=np.std(CIList)
    list_len=len(CIList)

    def calcErr(m,s,n):
        CI_lower=m - 1.96 *s/math.sqrt(n)
        CI_upper=m + 1.96 *s/math.sqrt(n)
        
        return CI_lower,CI_upper

    return(calcErr(list_mean,list_stdv,list_len))

#Exercise 3.9 (Functions that create functions) Create 
# a function that creates functions which take a list 
# of numbers as input and returns the 95% confidence 
# interval calculated. the correction factor  would be 
# 2.26 instead of 1.96.
fun=confInt(heights)
fun(1.96)
def confInt(CIList):   

    def inner(x):
        list_mean=np.mean(CIList)
        list_stdv=np.std(CIList)
        list_len=len(CIList)
        CI_lower=list_mean - x *list_stdv/math.sqrt(list_len)
        CI_upper=list_mean + x *list_stdv/math.sqrt(list_len)
        
        return CI_lower,CI_upper

    return(inner)


#Exercise 3.10 (Defining function defaults) Returning
# to confInt with the nested calcErr function
# modify the function so that we can input the error
# corrrection as an argument.
confInt(heights)
def  confInt(CIList):   

    list_mean=np.mean(CIList)
    list_stdv=np.std(CIList)
    list_len=len(CIList)

    def calcErr(m=177,s=10,n=6):
        CI_lower=m - 1.96 *s/math.sqrt(n)
        CI_upper=m + 1.96 *s/math.sqrt(n)
        
        return CI_lower,CI_upper

    return(calcErr(list_mean,list_stdv,list_len))


#Exercise 3.11 Modify the previous confInt function
# so that it accepts many lists instead of a single 
# list. It should combine all the values into one 
# large list.

#confInt(dist,heights)
#def  confInt(*args):   

 #   list_mean=np.mean(CIList)
  #  list_stdv=np.std(CIList)
   # list_len=len(CIList)
#
 #   def calcErr(m=177,s=10,n=6):
  #      CI_lower=m - 1.96 *s/math.sqrt(n)
   #     CI_upper=m + 1.96 *s/math.sqrt(n)
        
    #    return CI_lower,CI_upper

    #return(calcErr(list_mean,list_stdv,list_len))


#Exercise 3.12 Add a TypeError to the calcInt 
# function that returns a message if a list of
# strings is used as input.
confInt(cities) #string list
def  confInt(CIList):   

    try:
       list_mean=np.mean(CIList)
       list_stdv=np.std(CIList)
       list_len=len(CIList)
       CI_lower=list_mean - 1.96 *list_stdv/math.sqrt(list_len)
       CI_upper=list_mean + 1.96 *list_stdv/math.sqrt(list_len)
        
    except TypeError:
       print('nope, you have the wrong type')

    return CI_lower,CI_upper



#Exercise 3.13 Add a ValueError to the calcInt function 
# that returns a message if the maximum value is larger than 100.
confInt(heights)
def  confInt(CIList):   
    for x in CIList:
        if x > 100:
           raise ValueError('x maximum value is larger than 100.')
    try:
       list_mean=np.mean(CIList)
       list_stdv=np.std(CIList)
       list_len=len(CIList)
       CI_lower=list_mean - 1.96 *list_stdv/math.sqrt(list_len)
       CI_upper=list_mean + 1.96 *list_stdv/math.sqrt(list_len)
        
    except TypeError:
       print('nope, you have the wrong type')

    return CI_lower,CI_upper


#Exercise 3.14 (Composing sentences) “There is a 95% chance the the true 
# population parameter is covered by the region [XX, YY]” where XX and
# YY are the lower and upper limits of the 95% confidence interval,
# respectively.

confInt(heights)
def  confInt(CIList):   
    
    list_mean=np.mean(CIList)
    list_stdv=np.std(CIList)
    list_len=len(CIList)
    CI_lower=list_mean - 1.96 *list_stdv/math.sqrt(list_len)
    CI_upper=list_mean + 1.96 *list_stdv/math.sqrt(list_len)
    
    print(f"There is a 95% chance the the true population parameter is covered by the region {CI_lower , CI_upper}")

    return CI_lower,CI_upper


#Exercise 3.15 In class we’ll explore some of the uses. 
# Write examples for the remaining methods listed above.

dist.clear()#[]
dist.copy()
dist.count(584)
dist.extend()# Need an iterable object here:
dist.index(584)
dist.insert(1,99)
dist.reverse()

#Exercise 3.16 Returning to the two lists containing
# the cities and their distances
distDict = dict(zip(cities, dist))
distDict

#Exercise 4.2 (List to DataFrame) Returning 
# to the two lists containing the cities and
#  their distances from Berlin. Use the following 
# list of names to create a data frame with two
#  columns: city and dist

list_names = ['cities', 'dist']
list_cols = [cities, dist]

zip_list = list(zip(list_names, list_cols))
zip_list

zip_dict = dict(zip_list)
zip_dict
zip_df = pd.DataFrame(zip_dict)
zip_df

#Exercise 4.4 Select both the quantity and tissue columns
foo1 = [True, False, False, True, True, False]
foo2 = ["Liver", "Brain", "Testes", "Muscle", "Intestine", "Heart"]
foo3 = [13, 88, 1233, 55, 233, 18]

foo_df = pd.DataFrame({'healthy': foo1, 'tissue': foo2, 'quantity': foo3})
foo_df

foo_df[['healthy','tissue']]

#Exercise 4.5 Make a copy of foo_df, called foo_df_2.
#  Access the .columns and .index attributes and change
#  them to ['A', 'B', 'C'] and ['H', 'I', 'J', 'K', 'L', 'M'],
#  respectively.

foo_df_2 = foo_df.copy()
foo_df_2.columns= ['A', 'B', 'C']
foo_df_2.index=['H', 'I', 'J', 'K', 'L', 'M']
foo_df_2

#Exercise 5.1 Using foo_df, what commands would I use to get:
#The 2nd to 3rd rows?
foo_df.iloc[1:3,]
foo_df.iloc[[1, 2]]
#The last 2 rows?
foo_df[-2:]
#A random row in foo_df?
foo_df.sample()
#From the 4th to the last row? But without hard-coding,
#  i.e. regardless of how many rows my data frame contains
foo_df.iloc[3:,:]


#Exercise 5.2 List all the possible objects we can use inside iloc[]
foo_df.iloc[4,] #intger
foo_df.iloc[[1,4,-1,-1,3,2,0]] #list

#Exercise 5.3 (Indexing at intervals) Use indexing to obtain all
#  the odd and even rows only from the foo_df data frame.
foo_df.iloc[::2]#even
foo_df.iloc[1::2]#odd

foo_df[foo_df.index %2 ==0]
foo_df[foo_df.index %2 ==1]


#Exercise 5.4 Subset for boolean data:
#Only “healthy” samples.
foo_df[(foo_df.healthy == True)]
#Only “unhealthy” samples.
foo_df[(foo_df.healthy == False)]


#Exercise 5.5 Subset for numerical data:
#Only low quantity samples, those below 100.
foo_df[(foo_df.quantity <= 100)]
#Quantity between 100 and 1000,
foo_df[(foo_df.quantity > 100) & (foo_df.quantity < 1000)]
#Quantity below 100 and beyond 1000.
foo_df[(foo_df.quantity >= 1000) | (foo_df.quantity <= 100)]

#Exercise 5.6 Subset for strings:
#Only “heart” samples.
foo_df[(foo_df.tissue == "Heart")]
#“Heart” and “liver” samples
foo_df[(foo_df.tissue == "Heart")|(foo_df.tissue == "Liver")]
#Everything except “intestines”
foo_df[(foo_df.tissue != "Intestine")]


#Exercise 10.1 Using the cities list, below, 
# extract only those cities with long names, 
# over 6 characters long.

[x for x in cities if len(x) > 6]

#Exercise 10.2 Revisit the previous exercise, 
# but change the position of the logical expression.

[x if len(x) > 6 else 0 for x in cities]











