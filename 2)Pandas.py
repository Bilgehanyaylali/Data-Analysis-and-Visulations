# IMPORT PANDAS AND DATA READING #
import numpy as np
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option('display.expand_frame_repr', False)
df = pd.read_csv("supermarket.csv")
###############################

df.info()
"""class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 17 columns):
 #   Column                   Non-Null Count  Dtype  
---  ------                   --------------  -----  
 0   Invoice ID               1000 non-null   object 
 1   Branch                   1000 non-null   object 
 2   City                     1000 non-null   object 
 3   Customer type            1000 non-null   object 
 4   Gender                   1000 non-null   object 
 5   Product line             1000 non-null   object 
 6   Unit price               1000 non-null   float64
 7   Quantity                 1000 non-null   int64  
 8   Tax 5%                   1000 non-null   float64
 9   Total                    1000 non-null   float64
 10  Date                     1000 non-null   object 
 11  Time                     1000 non-null   object 
 12  Payment                  1000 non-null   object 
 13  cogs                     1000 non-null   float64
 14  gross margin percentage  1000 non-null   float64
 15  gross income             1000 non-null   float64
 16  Rating                   1000 non-null   float64
dtypes: float64(7), int64(1), object(9)
memory usage: 132.9+ KB"""

df.ndim
# 2

df.shape
# (1000, 17)

df.size
# 17000

# DATA OVERVIEW #

df.head()
""" Invoice ID Branch       City Customer type  Gender            Product line  Unit price ... 
0  750-67-8428      A     Yangon        Member  Female       Health and beauty       74.69 ...       
1  226-31-3081      C  Naypyitaw        Normal  Female  Electronic accessories       15.28 ...        
2  631-41-3108      A     Yangon        Normal    Male      Home and lifestyle       46.33 ...             
3  123-19-1176      A     Yangon        Member    Male       Health and beauty       58.22 ...           
4  373-73-7910      A     Yangon        Normal    Male       Sports and travel       86.31 ...  """

df.tail()
"""   Invoice ID Branch       City Customer type  Gender         Product line  Unit price  
995  233-67-5758      C  Naypyitaw        Normal    Male    Health and beauty       40.35  ...     
996  303-96-2227      B   Mandalay        Normal  Female   Home and lifestyle       97.38  ...     
997  727-02-1313      A     Yangon        Member    Male   Food and beverages       31.84  ...       
998  347-56-2442      A     Yangon        Normal    Male   Home and lifestyle       65.82  ...       
999  849-09-3807      A     Yangon        Member  Female  Fashion accessories       88.34  ... """

df.columns
"""
Index(['Invoice ID', 'Branch', 'City', 'Customer type', 'Gender',
       'Product line', 'Unit price', 'Quantity', 'Tax 5%', 'Total', 'Date',
       'Time', 'Payment', 'cogs', 'gross margin percentage', 'gross income',
       'Rating'],
      dtype='object')"""

df.describe().T
"""                      count        mean           std        min         25%         50%         75%          max
Unit price               1000.0   55.672130  2.649463e+01  10.080000   32.875000   55.230000   77.935000    99.960000
Quantity                 1000.0    5.510000  2.923431e+00   1.000000    3.000000    5.000000    8.000000    10.000000
Tax 5%                   1000.0   15.379369  1.170883e+01   0.508500    5.924875   12.088000   22.445250    49.650000
Total                    1000.0  322.966749  2.458853e+02  10.678500  124.422375  253.848000  471.350250  1042.650000
cogs                     1000.0  307.587380  2.341765e+02  10.170000  118.497500  241.760000  448.905000   993.000000
gross margin percentage  1000.0    4.761905  6.131498e-14   4.761905    4.761905    4.761905    4.761905     4.761905
gross income             1000.0   15.379369  1.170883e+01   0.508500    5.924875   12.088000   22.445250    49.650000
Rating                   1000.0    6.972700  1.718580e+00   4.000000    5.500000    7.000000    8.500000    10.000000"""

df.isnull().values.any()
# False

df.isnull().values
"""array([[False, False, False, ..., False, False, False],
       [False, False, False, ..., False, False, False],
       [False, False, False, ..., False, False, False],
       ...,
       [False, False, False, ..., False, False, False],
       [False, False, False, ..., False, False, False],
       [False, False, False, ..., False, False, False]])"""

df.isnull().sum()
"""
Invoice ID                 0
Branch                     0
City                       0
Customer type              0
Gender                     0
Product line               0
Unit price                 0
Quantity                   0
Tax 5%                     0
Total                      0
Date                       0
Time                       0
Payment                    0
cogs                       0
gross margin percentage    0
gross income               0
Rating                     0
dtype: int64"""

df.index
# RangeIndex(start=0, stop=1000, step=1)

df[0:13]
""" Invoice ID      Branch     City Customer type  Gender            Product line  Unit price  ...
0   750-67-8428      A     Yangon        Member  Female       Health and beauty       74.69    ...     
1   226-31-3081      C  Naypyitaw        Normal  Female  Electronic accessories       15.28    ...    
2   631-41-3108      A     Yangon        Normal    Male      Home and lifestyle       46.33    ...     
3   123-19-1176      A     Yangon        Member    Male       Health and beauty       58.22    ...   
4   373-73-7910      A     Yangon        Normal    Male       Sports and travel       86.31    ...     
5   699-14-3026      C  Naypyitaw        Normal    Male  Electronic accessories       85.39    ...    
6   355-53-5943      A     Yangon        Member  Female  Electronic accessories       68.84    ...    
7   315-22-5665      C  Naypyitaw        Normal  Female      Home and lifestyle       73.56    ...   
8   665-32-9167      A     Yangon        Member  Female       Health and beauty       36.26    ...     
9   692-92-5582      B   Mandalay        Member  Female      Food and beverages       54.84    ...     
10  351-62-0822      B   Mandalay        Member  Female     Fashion accessories       14.48    ...    
11  529-56-3974      B   Mandalay        Member    Male  Electronic accessories       25.51    ...    
12  365-64-0515      A     Yangon        Normal  Female  Electronic accessories       46.95    ...     """

df.drop(0, axis=0)
"""   Invoice ID Branch       City Customer type  Gender            Product line  Unit price  ...  
1    226-31-3081      C  Naypyitaw        Normal  Female  Electronic accessories       15.28  ...      
2    631-41-3108      A     Yangon        Normal    Male      Home and lifestyle       46.33  ...      
"""

df.drop("City", axis=1)
"""   Invoice ID    Branch Customer type  Gender       Product line               Unit price  Quantity  ... 
0    750-67-8428      A        Member     Female       Health and beauty            74.69         7     ...
1    226-31-3081      C        Normal     Female       Electronic accessories       15.28         5     ...  """

df.drop([1, 3, 5, 7, 9], axis=0).head()
"""   Invoice ID Branch    City Customer type  Gender            Product line  Unit price ...
0  750-67-8428      A  Yangon        Member  Female       Health and beauty       74.69   ...   
2  631-41-3108      A  Yangon        Normal    Male      Home and lifestyle       46.33   ...     
4  373-73-7910      A  Yangon        Normal    Male       Sports and travel       86.31   ...    
6  355-53-5943      A  Yangon        Member  Female  Electronic accessories       68.84   ...      
8  665-32-9167      A  Yangon        Member  Female       Health and beauty       36.26   ...   """

df.index = df["Invoice ID"]
df.head()
"""             Invoice ID Branch       City Customer type  Gender            Product line  ...
Invoice ID                                                                                  ...                                                                                                                           
750-67-8428  750-67-8428      A     Yangon        Member  Female       Health and beauty    ...   
226-31-3081  226-31-3081      C  Naypyitaw        Normal  Female  Electronic accessories    ...   
631-41-3108  631-41-3108      A     Yangon        Normal    Male      Home and lifestyle    ... 
123-19-1176  123-19-1176      A     Yangon        Member    Male       Health and beauty    ...   
373-73-7910  373-73-7910      A     Yangon        Normal    Male       Sports and travel    ... """

df = df.reset_index(drop=True)
df.head()
"""Invoice ID     Branch     City Customer type  Gender            Product line  Unit price  ...
0   750-67-8428      A     Yangon        Member  Female       Health and beauty       74.69    ...     
1   226-31-3081      C  Naypyitaw        Normal  Female  Electronic accessories       15.28    ...    
2   631-41-3108      A     Yangon        Normal    Male      Home and lifestyle       46.33    ...     
3   123-19-1176      A     Yangon        Member    Male       Health and beauty       58.22    ...   
4   373-73-7910      A     Yangon        Normal    Male       Sports and travel       86.31    ...     
5   699-14-3026      C  Naypyitaw        Normal    Male  Electronic accessories       85.39    ...  """

"City" in df
# True

print(type(df["City"]))
# <class 'pandas.core.series.Series'>

print(type(df[["City"]]))
# <class 'pandas.core.frame.DataFrame'>


print(df.loc[:, df.columns.str.contains("City")].head())
"""     City
0     Yangon
1  Naypyitaw
2     Yangon
3     Yangon
4     Yangon"""

# LOC & ILOC #

df.iloc[0:3]
"""  Invoice ID Branch      City Customer type  Gender            Product line  Unit price   ...
0  750-67-8428      A     Yangon        Member  Female       Health and beauty       74.69   ...     
1  226-31-3081      C  Naypyitaw        Normal  Female  Electronic accessories       15.28   ...      
2  631-41-3108      A     Yangon        Normal    Male      Home and lifestyle       46.33   ...     
 """

df.iloc[0:3, 0:2]
"""    
    Invoice ID Branch
0  750-67-8428      A
1  226-31-3081      C
2  631-41-3108      A"""

df.loc[0:3, "Gender"]
"""
0    Female
1    Female
2      Male
3      Male
Name: Gender, dtype: object"""

# CONDITIONAL EXPRESSIONS #

df[df["Unit price"] > 50].head()
""" Invoice ID  Branch     City   Customer type   Gender            Product line  Unit price  ...
0  750-67-8428      A     Yangon        Member  Female       Health and beauty       74.69    ...     
3  123-19-1176      A     Yangon        Member    Male       Health and beauty       58.22    ...     
4  373-73-7910      A     Yangon        Normal    Male       Sports and travel       86.31    ...     
5  699-14-3026      C  Naypyitaw        Normal    Male  Electronic accessories       85.39    ...     
6  355-53-5943      A     Yangon        Member  Female  Electronic accessories       68.84    ... """

df[df["Unit price"] > 50].count()
"""
Invoice ID                 561
Branch                     561
City                       561
Customer type              561
Gender                     561
Product line               561
Unit price                 561
Quantity                   561
Tax 5%                     561
Total                      561
Date                       561
Time                       561
Payment                    561
cogs                       561
gross margin percentage    561
gross income               561
Rating                     561
dtype: int64"""

df[df["Unit price"] > 50]["City"].count()
# 561

df.loc[df["Unit price"] > 50, ["Unit price", "City"]].head()
"""   Unit price    City
0       74.69     Yangon
3       58.22     Yangon
4       86.31     Yangon
5       85.39  Naypyitaw
6       68.84     Yangon"""

df.loc[(df["Unit price"] > 50) & (df["Branch"] == "A"), ["Unit price", "Payment"]].head()
""" Unit price  Payment
0        74.69  Ewallet
3        58.22  Ewallet
4        86.31  Ewallet
6        68.84  Ewallet
14       71.38    Cash"""

# AGGREGATION AND GROUPING #


df["Unit price"].mean()
# 55.67213

df.groupby("City")["Unit price"].mean()
"""City
Mandalay     55.659277
Naypyitaw    56.609024
Yangon       54.780853
Name: Unit price, dtype: float64"""

df.groupby("Gender").agg({"Unit price": "mean"})
"""     Unit price
Gender            
Female   55.263952
Male     56.081944"""

df.groupby("Gender").agg({"Unit price": ["mean", "max", "sum", "min", "std"]})
"""       Unit price                                   
         mean    max       sum    min        std
Gender                                              
Female  55.263952  99.73  27687.24  10.16  27.194037
Male    56.081944  99.96  27984.89  10.08  25.794145
"""

df.groupby("Gender").agg({"Unit price": ["mean", "max", "sum", "min", "std"],
                          "Total": ["mean", "max"],
                          "Product line": "count"})
"""     
        Unit price                                         Total          Product line
             mean    max       sum    min        std        mean      max        count
Gender                                                                                
Female  55.263952  99.73  27687.24  10.16  27.194037  335.095659  1042.65          501
Male    56.081944  99.96  27984.89  10.08  25.794145  310.789226  1039.29          499
"""

# PIVOT TABLE #


df.pivot_table("Rating", "Gender", "City")
"""
City    Mandalay  Naypyitaw    Yangon
Gender                               
Female  6.876543   7.157865  6.839130
Male    6.762353   6.972000  7.196089"""

df.pivot_table("Rating", "Gender", "City", aggfunc="std")
"""
City    Mandalay  Naypyitaw    Yangon
Gender                               
Female  1.825987   1.700638  1.735986
Male    1.602880   1.709316  1.714425"""

df.pivot_table("Rating", "Gender", ["City", "Customer type"])
"""
City           Mandalay            Naypyitaw             Yangon          
Customer type    Member    Normal    Member    Normal    Member    Normal
Gender                                                                   
Female         6.885882  6.866234  7.117708  7.204878  6.786250  6.891358
Male           6.647500  6.864444  6.957534  6.985714  7.194253  7.197826"""

# CONCAT AND MERGE #

m = np.random.randint(1, 30, size=(5, 5))
"""array([[ 1, 15, 17,  5, 25],
       [25,  2, 14, 12, 28],
       [25, 15, 20, 20, 22],
       [11, 13,  5, 27, 21],
       [22, 14, 18, 10, 23]])"""

df_1 = pd.DataFrame(m, columns=["var1", "var2", "var3", "var4", "var5"])
"""   var1  var2  var3  var4  var5
0     1    15    17     5    25
1    25     2    14    12    28
2    25    15    20    20    22
3    11    13     5    27    21
4    22    14    18    10    23"""

df_2 = df_1 * 10
"""   var1  var2  var3  var4  var5
0    10   150   170    50   250
1   250    20   140   120   280
2   250   150   200   200   220
3   110   130    50   270   210
4   220   140   180   100   230"""

##################

df_3 = pd.concat([df_1, df_2])
"""   var1  var2  var3  var4  var5
0     1    15    17     5    25
1    25     2    14    12    28
2    25    15    20    20    22
3    11    13     5    27    21
4    22    14    18    10    23
0    10   150   170    50   250
1   250    20   140   120   280
2   250   150   200   200   220
3   110   130    50   270   210
4   220   140   180   100   230
"""

df_3 = pd.concat([df_1, df_2], ignore_index=True)
"""   var1  var2  var3  var4  var5
0     1    15    17     5    25
1    25     2    14    12    28
2    25    15    20    20    22
3    11    13     5    27    21
4    22    14    18    10    23
5    10   150   170    50   250
6   250    20   140   120   280
7   250   150   200   200   220
8   110   130    50   270   210
9   220   140   180   100   230"""

df_4 = pd.concat([df_1, df_2], axis=1)
"""   var1  var2  var3  var4  var5  var1  var2  var3  var4  var5
0     1    15    17     5    25    10   150   170    50   250
1    25     2    14    12    28   250    20   140   120   280
2    25    15    20    20    22   250   150   200   200   220
3    11    13     5    27    21   110   130    50   270   210
4    22    14    18    10    23   220   140   180   100   230"""

df_5 = pd.concat([df_1, df_2], ignore_index=True, axis=1)
"""   
    0   1   2   3   4    5    6    7    8    9
0   1  15  17   5  25   10  150  170   50  250
1  25   2  14  12  28  250   20  140  120  280
2  25  15  20  20  22  250  150  200  200  220
3  11  13   5  27  21  110  130   50  270  210
4  22  14  18  10  23  220  140  180  100  230"""


