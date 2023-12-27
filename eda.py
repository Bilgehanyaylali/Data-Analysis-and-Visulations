# Advanced Functional Exploratory Data Analysis (EDA)

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = pd.read_csv("supermarket.csv")


def check_df(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### Tail #####################")
    print(dataframe.tail(head))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)


check_df(df)
# Analysis of Categorical Variables #
#################################
# I find object,categorical,numerical columns

categorical_columns = [i for i in df.columns if str(df[i].dtypes) in ['object', 'category', 'bool']]
# ['Invoice ID', 'Branch', 'City', 'Customer type', 'Gender', 'Product line', 'Date', 'Time', 'Payment']
numerical_columns = [i for i in df.columns if str(df[i].dtypes) in ["float64", "int64"]]
# ['Unit price', 'Quantity', 'Tax 5%', 'Total', 'cogs', 'gross margin percentage', 'gross income', 'Rating']

# Some categorical columns are useless for analyse so i drop some of them.
categorical_columns.remove('Invoice ID')
categorical_columns.remove('Date')
categorical_columns.remove('Time')


# Categorical columns summary #
def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("################################################")


# I add loops

for i in categorical_columns:
    cat_summary(df, i)

"""Branch        Ratio
 Branch               
 A          340   34.0
 B          332   33.2
 C          328   32.8
################################################
           City  Ratio
City                  
Yangon      340   34.0
Mandalay    332   33.2
Naypyitaw   328   32.8
################################################
               Customer type  Ratio
Customer type                      
Member                   501   50.1
Normal                   499   49.9
################################################
        Gender  Ratio
Gender               
Female     501   50.1
Male       499   49.9
################################################
                        Product line  Ratio
Product line                               
Fashion accessories              178   17.8
Food and beverages               174   17.4
Electronic accessories           170   17.0
Sports and travel                166   16.6
Home and lifestyle               160   16.0
Health and beauty                152   15.2
################################################
             Payment  Ratio
Payment                    
Ewallet          345   34.5
Cash             344   34.4
Credit card      311   31.1
################################################"""


# Categorical columns' Visualization #

def cat_summary2(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("################################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)


# I add loops
for i in categorical_columns:
    cat_summary2(df, i, plot=True)


# I will add graphics visualizations in kaggle #

# Analysis of Numerical Variables #

def num_summary(dataframe, col_name):
    print(dataframe[col_name].describe().T)


num_summary(df, numerical_columns)

"""                        count        mean           std        min         25%         50%         75%          max
Unit price               1000.0   55.672130  2.649463e+01  10.080000   32.875000   55.230000   77.935000    99.960000
Quantity                 1000.0    5.510000  2.923431e+00   1.000000    3.000000    5.000000    8.000000    10.000000
Tax 5%                   1000.0   15.379369  1.170883e+01   0.508500    5.924875   12.088000   22.445250    49.650000
Total                    1000.0  322.966749  2.458853e+02  10.678500  124.422375  253.848000  471.350250  1042.650000
cogs                     1000.0  307.587380  2.341765e+02  10.170000  118.497500  241.760000  448.905000   993.000000
gross margin percentage  1000.0    4.761905  6.131498e-14   4.761905    4.761905    4.761905    4.761905     4.761905
gross income             1000.0   15.379369  1.170883e+01   0.508500    5.924875   12.088000   22.445250    49.650000
Rating                   1000.0    6.972700  1.718580e+00   4.000000    5.500000    7.000000    8.500000    10.000000"""


# Numerical columns' Visualization #

def num_summary2(dataframe, col_name, plot=False):
    print(dataframe[col_name].describe().T)
    if plot:
        dataframe[col_name].hist()
        plt.xlabel(col_name)
        plt.title(col_name)
        plt.show(block=True)


for i in numerical_columns:
    num_summary2(df, i, plot=True)

# I will add graphics visualizations in kaggle #

#####################################################
# Analysis of Target Variable with Categorical variables #
# My target variable is Customer Type, so I will change these columns  boolean for easy analysis #

df['Customer type'].replace({'Member': 1, 'Normal': 0}, inplace=True)

df["Customer type"].value_counts()
"""Customer type
1    501
0    499"""


######################################

def target_sum_cat(dataframe, target, categorical_columns):
    print(pd.DataFrame({"Target Mean": dataframe.groupby(categorical_columns)[target].mean()}), end="\n\n\n")


target_sum_cat(df, "Customer type", "Gender")
"""        Target Mean
Gender             
Female     0.520958
Male       0.480962
"""

# With loops #
for i in categorical_columns:
    target_sum_cat(df, "Customer type", i)

"""      Target Mean
Branch             
A          0.491176
B          0.496988
C          0.515244
           Target Mean
City                  
Mandalay      0.496988
Naypyitaw     0.515244
Yangon        0.491176
               Target Mean
Customer type             
0                      0.0
1                      1.0
        Target Mean
Gender             
Female     0.520958
Male       0.480962
                        Target Mean
Product line                       
Electronic accessories     0.458824
Fashion accessories        0.483146
Food and beverages         0.540230
Health and beauty          0.480263
Home and lifestyle         0.518750
Sports and travel          0.524096
             Target Mean
Payment                 
Cash            0.488372
Credit card     0.553055
Ewallet         0.466667
"""


# Analysis of Target Variable with Numerical variables #

df['Customer type'].replace({1: 'Member', 0: 'Normal'}, inplace=True)


def target_sum_num(dataframe, target, numerical_columns):
    print(dataframe.groupby(target).agg({numerical_columns: "mean"}), end="\n\n\n")
    print("###############################")


target_sum_num(df, "Customer type", "Quantity")
"""               Quantity
Customer type          
Member         5.558882
Normal         5.460922
"""

# With loops #

for i in numerical_columns:
    target_sum_num(df, "Customer type", i)

"""               Unit price
Customer type            
Member          56.206986
Normal          55.135130
###############################
               Quantity
Customer type          
Member         5.558882
Normal         5.460922
###############################
                  Tax 5%
Customer type           
Member         15.609110
Normal         15.148707
###############################
                    Total
Customer type            
Member         327.791305
Normal         318.122856
###############################
                     cogs
Customer type            
Member         312.182196
Normal         302.974148
###############################
               gross margin percentage
Customer type                         
Member                        4.761905
Normal                        4.761905
###############################
               gross income
Customer type              
Member            15.609110
Normal            15.148707
###############################
                 Rating
Customer type          
Member         6.940319
Normal         7.005210
###############################"""