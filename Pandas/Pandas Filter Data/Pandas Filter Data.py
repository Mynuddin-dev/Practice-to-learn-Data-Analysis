#!/usr/bin/env python
# coding: utf-8


import pandas as pd

data = pd.read_csv("master.csv")
data
data.country
data.country.unique()
data.country.unique().size
data.country.size

suicide_data = data["suicides_no"]
suicide_data

suicide_data.max()


data.country == "Israel"
type(data.country == "Israel")

data [data.country == "Israel"]

type(data [data.country == "Israel"])

data [(data.country == "Israel") &  (data.year == 2014)]

data [(data.country == "Israel") &  (data.year == 2014) & (data.sex == "female")]

data [(data.country == "Israel") &  (data.year == 2014) & (data.sex == "male")]

mask1 = data.country == "Israel"
mask2 = data.year == 2014
mask3 = data.sex=="male"
data[mask1 & mask2 & mask3]


mask1 = data.country == "Israel"
mask2 = data.year == 2014
mask3 = data.sex=="male"
data.loc[mask1 & mask2 & mask3,["country","year","sex","age"]]

data.sum().suicides_no

data.max().suicides_no

data[data.suicides_no==22338]

mask1 = data.country == "Israel"
mask2 = data.year == 2014
mask3 = data.sex=="male"
#mask3 = data.sex=="female"
df = data.loc[mask1 & mask2 & mask3,["country","year","sex","age","suicides_no"]]

df.sum().suicides_no

type(df)

df.max().suicides_no

# # Part 2

data.loc[data.year >= 2010]

#mask = data.year.between(1999,2000)
mask = data.year.between(2000,2010)

data.loc[mask]



data.loc[data.year.isin([2000,2010])]
         


data.loc[~(data.year.isin([2000,2010]))]     
# without 2000 and 2010


data.loc[~(data.year.isin([2000,2010]))].year.unique()


maski = data.year.between(2010,2016)
maski1 = data.sex =="male"
maski2 = data.country =="Switzerland"
maski3 = data.age =="25-34 years"
data.loc[maski & maski1 & maski2 & maski3,["country","year","sex","age","suicides_no"]]



f = data.loc[maski & maski1 & maski2 & maski3,["country","year","sex","age","suicides_no"]].sum().suicides_no
f


g = data.loc[maski & (data.sex=="female") & maski2 & maski3,["country","year","sex","age","suicides_no"]].sum().suicides_no


g

print(f"Male suicide -> {f}\nFemale suicide -> {g}" )





