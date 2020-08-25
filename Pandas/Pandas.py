
import pandas as pd

movies_data = pd.read_csv("tmdb_5000_movies.csv")


print(movies_data)


type(movies_data)

print(movies_data.shape)

movies_data.columns

movies_data.index

movies_data.head

movies_data.tail

movies_data.head(10)

movies_data.tail(20)

movies_data.info()

movies_data.describe()


# Selecting columns

print(movies_data.head)
print(movies_data.head())


print(movies_data["budget"])

# For multiple column you need to pass a list
print(movies_data[["budget" , "original_title"]])
print(movies_data[["budget" , "original_title","status"]])

type(movies_data[["budget" , "original_title","status"]])
type(movies_data["budget"])

print(movies_data["budget"])
print(movies_data[["budget"]])

print(movies_data[["budget" , "original_title","status","tagline","runtime","release_date","revenue"]])
# order maintain




# Selecting rows using square brackets


print(movies_data[0:1])
print(movies_data[5:32])     # u can store it a variable

print(movies_data[5:32][["budget","revenue"]])   # row and column
print(movies_data[5:32][0:3]) 

data = movies_data[5:10]
print(data)
print(data[["budget","revenue"]])


# ----------------------------iloc -----------------------------------------
# recomended
print(movies_data.iloc[0])
print(type(movies_data.iloc[0]))

print(movies_data.iloc[0:5])
print(type(movies_data.iloc[0:5]))
print(movies_data.iloc[[0,3,5,7,9,10]])  # pass list

# serieas is a single(one dimension) column or row of excel dataset
# DataFrame is two-dimensional size-mutable, potentially heterogeneous tabular 
# data structure with labeled axes (rows and columns).
# A Data frame is a two-dimensional data structure
# DataFrame consists of three principal components, the data, rows, and columns.


print(movies_data.iloc[[0,2,5,6,8,9],[1,6,9]])     # Row and column

print(movies_data.iloc[[0,2,5,6,8,9],0:6])     
print(movies_data.iloc[0:10,0:2])

print(movies_data.iloc[0:10,0:10])


#------------------------------------ loc -----------------------------------

print(movies_data.loc[3])
print(movies_data.loc[0:3])  # 3 included
print(movies_data.iloc[0:4]) # 4 not included


movies_data1 = pd.read_csv("tmdb_5000_movies.csv" , index_col="original_title")
movies_data1
movies_data1.columns

movies_data1.loc["Avatar"]
# movies_data.loc["Avatar"] Error

movies_data1.loc[["Avatar","Spectre"]]



# World Happiness rank report exercise

happy_data = pd.read_csv("2019 World happiness.csv")
happy_data
happy_data.head(5)
happy_data.tail(5)
happy_data.columns
happy_data.columns.size
happy_data.index
happy_data.iloc[4:10]
happy_data.info()
happy_data1 = pd.read_csv("2019 World happiness.csv" , index_col = "Country or region")
happy_data1
happy_data1.head()
happy_data1.loc[["Japan", "India" , "Pakistan"]]
happy_data1.loc[["Japan", "Pakistan" ,"India"],"Overall rank"]







# Series


# serieas is a single(one dimension) column or row of excel dataset
# DataFrame is two-dimensional size-mutable, potentially heterogeneous tabular 
# data structure with labeled axes (rows and columns).
# A Data frame is a two-dimensional data structure
# DataFrame consists of three principal components, the data, rows, and columns.



print(movies_data.head())
print(type(movies_data.head()))

print(movies_data["budget"])
print(type(movies_data["budget"]))


print(movies_data.iloc[0])
print(type(movies_data.iloc[0]))

# ser = movies_data["budget"]
ser = movies_data["runtime"]

ser.head(5)
ser.tail()
ser.head()
ser.tail(10)
ser.dtype

ser.shape
ser.size
ser.describe()
ser.index
type(ser)
ser.sum()
ser.count()
ser. size - ser.count()

movies_data.info()
# ser.info()  Error

ser.mean()
ser.std()
ser.median()
ser.min()
ser.max()
ser.unique()    # use only in series not dataframe
ser.unique().size
ser.nunique(dropna=True)
ser.nunique(dropna=False)
ser.nunique()

movies_data.nunique()

ser.value_counts()
ser.value_counts(ascending=True)
ser.value_counts(bins=3)
ser.value_counts(bins=10)


# https://www.geeksforgeeks.org/introduction-to-pandas-in-python/?ref=lbp
# Different ways to creat series
import numpy as np


# a = np.array(["P","y","t","h","o","n"])
# b = ["P","a","n","d","a","s"]

a = np.array(["P","y","t","h","o","n"])
b = ("P","a","n","d","a","s")

# a = ["P","y","t","h","o","n"]
# b = ["P","a","n","d","a","s"]

ser1 = pd.Series(a , name="Creating a series")
ser1
type(ser1)

ser2 = pd.Series(a , index = b ,name="Creating a series")
ser2

dic = {
        "P" : "P",
        "a" : "y",
        "n" : "t",
        "d" : "h",
        "a_" : "o",
        "s" : "n"
       }

ser3 = pd.Series(dic , name="Creating a series")
ser3

# ser4 = pd.read_csv("tmdb_5000_movies.csv" , usecols=["budget","genres"])
# ser4 = pd.read_csv("tmdb_5000_movies.csv" , usecols=["budget"])

# ser4
# type(ser4)

ser4 = pd.read_csv("tmdb_5000_movies.csv" , usecols=["budget"] , squeeze=True)
ser4
type(ser4)


# Series sort

d = {2 : "Two"  , 1 : "One" , 3 : "Three" , 4 : "Four"}

ser5 = pd.Series(d , name = " Numbers")
ser5

ser5.sort_index()
ser5.sort_index(ascending=True)
ser5.sort_index(ascending=False)

ser5.sort_index(ascending=True , inplace=True)
ser5

ser5.sort_values() # alphabatially sort
ser5.sort_values(ascending=True , inplace=True)
ser5



ser5.tolist()     # convert into a list
ser5.values       # convert into an array
type(ser5.values)




data1 = movies_data["vote_count"]

data1.nsmallest().index[0]
data1.nsmallest()  
data1.nsmallest(20)    # Ascending order


data1.nlargest().index[0]
data1.nlargest()  
data1.nlargest(20)    # Ascending order









# Index Object

import pandas as pd

movies_df = pd.read_csv("tmdb_5000_movies.csv" , index_col="original_title")

print(movies_df.head())
movies_df.loc["Spectre"]

movies_df.reset_index()
movies_df.head()

movies_df.reset_index(inplace=True)
movies_df.head()


movies_df.set_index("homepage")
movies_df.head()

# movies_df.set_index("homepage" , inplace=True)
movies_df.set_index("original_title" , inplace=True)

movies_df.head()

movies_df.index
movies_df.columns

type(movies_df.index)
type(movies_df.columns)

movies_df.index[0]
movies_df.index[0:4]
movies_df.index[5]

movies_df.columns[0]
movies_df.columns[0:4]
movies_df.columns[3]

movies_df.columns[-2]   # 2nd last
movies_df.columns[-2:]
movies_df.index[-2:]


movies_df.index.get_loc("My Date with Drew")
movies_df.index.get_loc("Spectre")


movies_df.columns.get_loc("id")
movies_df.columns.get_loc("genres")


movies_df.columns.is_unique
movies_df.index.is_unique
 

# Create index object

xyz = pd.Index(["A","B","C" , "D"])
xyz
type(xyz)










