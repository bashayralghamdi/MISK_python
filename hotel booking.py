
# Import an entire library and give it an alias
import pandas as pd # For DataFrame and handling
import numpy as np # Array and numerical processing
import math# Functions beyond the basic maths
import matplotlib.pyplot as plt # Low level plotting
import seaborn as sns # High level Plotting

#Import the data set and assign it to the variable hotels.
hotels =pd.read_csv('data/hotels.csv')

#describtion of the dataset:
hotels.shape # number of columns and index 
hotels.info()# The object
hotels.head() # explore first dataset rows
hotels.columns # columns names
hotels.describe() # # Summaries for all columns

#So we do not need to use all of these columns, we need some specific columns
#select the columns that we need
hotels_ss = hotels.loc[:,['hotel','is_canceled','arrival_date_month','adults','children','babies','customer_type','stays_in_weekend_nights','stays_in_week_nights',]]

#describtion of the dataset:
hotels_ss.shape # number of columns and index 
hotels_ss.info()# The object
hotels_ss.head() # explore first dataset rows
hotels_ss.columns # columns names
hotels_ss.describe() # # Summaries for all columns

#if there any missing value
hotels_ss.isnull().sum()
#remove missing value 
hotels_ss=hotels_ss.dropna(how='any')

#Percentage of which month is there more reservation
#the result is August is the most month that had more reservation .
# in the other hand January is the lowest.
sns.countplot(x='arrival_date_month',data=hotels_ss)

#her for each month what is the percentage between who has kids or not.
#create new column that calculat the sum of the kids (baby + children)
hotels_ss['kids']=hotels_ss['children']+hotels_ss['babies']

#convert the kids column to if there or not
for ind,row in hotels_ss.iterrows():
    if hotels_ss.loc[ind,'kids']==0 :
        hotels_ss.loc[ind,'kids']='have not'
    else:
        hotels_ss.loc[ind,'kids']='have'

#data visiualaization for each month 
sns.countplot(x='arrival_date_month',data=hotels_ss,hue='kids')

#Chapter 12 Portfolio-Building Project, Functions
#upper and lower limit 95% CI  of adr column 
#calling method
confInt(hotels.adr)

#convert the kids column to if there or not
#call method
for ind,row in hotels_ss.iterrows():
    havekids(ind,hotels_ss)
    

#method for new column that have kids or not
def  havekids(ind,hotels_ss):   

    if hotels_ss.loc[ind,'kids'] == 0 :
        hotels_ss.loc[ind,'kids'] = 'have not'
    else:
        hotels_ss.loc[ind,'kids'] = 'have'


#method for #upper and lower limit 95% CI  of adr column 
def  confInt(CIList):   

    list_mean=np.mean(CIList)
    list_stdv=np.std(CIList)
    list_len=len(CIList)

    def calcErr(m=177,s=10,n=6):
        CI_lower=m - 1.96 *s/math.sqrt(n)
        CI_upper=m + 1.96 *s/math.sqrt(n)
        
        return CI_lower,CI_upper

    return(calcErr(list_mean,list_stdv,list_len))

#Chapter 14 Portfolio-Building Project, OOP

#create class for new column that have kids or not
class HaveKids:
    """This is my new class for new column 
         that about have kids or not"""

    def  havekids(self,ind,hotels_ss): 
        if hotels_ss.loc[ind,'kids'] == 0 :
            hotels_ss.loc[ind,'kids'] = 'have not'
        else:
            hotels_ss.loc[ind,'kids'] = 'have'

    @classmethod
    def classmethod(cls):
        return 'class method called cls = ', cls

#create class object 
A=HaveKids()

#call method
for ind,row in hotels_ss.iterrows():
    A.havekids(ind,hotels_ss)






