# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 09:15:28 2020

@author: Mynuddin
"""
"""5 Creat array""" 

import numpy  as np

# list1 = [1,2,3,4]
list1 = [[[1,2,3,4],[5,6,7,8]],
         [[1,2,3,4],[5,6,7,8]]]

# list1 = [[1,2,3,4],[5,6,7,8]]
print(list1)
print(type(list1))

arr = np.array(list1)
print(arr )
print(type(arr))
print(arr.shape)
print(arr.ndim)

""" 6 Creat Numpy array using Numpy function"""

# zero , ones , diag , randint , rand , randn

# arr = np.zeros(5)
# arr = np.zeros((2,3))
# arr = np.zeros((2 ,2,2))
# print(arr)

# arr = np.ones(5)
# arr = np.ones((2,3))
# arr = np.ones((2 ,2,2))
# print(arr)


# arr = np.eye(4)  # 2D Matrix > 4x4 > diagonal ->1 others 0
# print(arr)

# arr = np.eye(5,4)
# print(arr)


# arr = np.diag([1,2,3,4])    # 4 x 4
# print(arr)
arr = np.diag([1,2,3,4,5,6])  # 6 x 6
print(arr)
print(np.diag(arr))


# rand_array = np.random.randint(1,15 , 4)   #Start, Stop(Exclusive) value
# print(rand_array) 


# rand_array = np.random.rand(4)  
# print(rand_array) 

# rand_array = np.random.rand(10)  
# print(rand_array) 

# rand_array = np.random.rand(2,3)  
# print(rand_array) 


rand_array = np.random.randn(4)  
print(rand_array) 

rand_array = np.random.randn(40000)  
print(np.mean(rand_array) ) # close to 0



""" Reshapping of Data """

arr = np.random.randint(1,101,20)
print(arr)
print(arr.ndim)
print(type(arr))
print(arr.shape)

print(arr.reshape(4,5))
print(arr.shape)

# arr1 = arr.reshape(2,10)
# print(arr1)
# print(arr1.shape)

arr1 = arr.reshape(5,4)
print(arr1)
print(arr1.shape)
print(arr1.ndim)


print(arr1.reshape(20))


arr2 = np.random.randint(1,101,30)
print(arr2)
arr2 = arr2.reshape(2,3,5)
# arr2 = arr2.reshape(2,3,-1) #(2, 3, 5) what should be it should be
# arr2 = arr2.reshape(2,-1,5) #(2, 3, 5) what should be it should be
# its creat auto

print(arr2)
print(arr2.ndim)
print(arr2.shape)
 
# But for 
print(arr2.reshape(-1)) # as like flatten ravel


""" seed() how to generate same randome num """

np.random.seed(12)  # it should be run first
ar = np.random.randint(1,21,10)
print(ar)

np.random.seed(12) 
ar1 = np.random.randint(1,21,10)
print(ar1)
print(ar.size)


# 10 Indexing and Slicing 1-D Array
Ar = np.array([4,2,9,4,5,7])

Ar[0]
Ar[1]
Ar[4]
Ar[:]

Ar[1:4]
Ar[1:4:1]
Ar[1:4:2]
Ar[1::2]


Ar[0:]
Ar[-3]
Ar[:4]
Ar[2:]
Ar[2:5]
Ar[-1]
Ar[:-5]
Ar[-5:-2]






# 11 Indexing and Slicing 2-D Array

array = np.array([[1,2,3,4],[9,8,7,6],[5,4,3,2]])
print(array)

# Double Bracket
print(array[0][1])
print(array[2][3])


# Single Brackrt --> Recomended
print(array[0,1])
print(array[1,2])
print(array[1,1])

print(array[:2 , :2])
print(array[1: , 1:])
print(array[1: , 2:])

np.random.seed(123)
matrix = np.random.randint(1,101,30).reshape(5,6)
print(matrix)

# 86 95
# 41 4
print(matrix[1:3 , 1:3])

# 35 98
# 65 76
print(matrix[1:3 , 4:])

# 11 23
# 31 53
print(matrix[3: , 2:4])


# 65 76
# 78 19
print(matrix[2:4 , 4:])

print(matrix[1:4 , 1:5])





# 12 view() vs copy()

Ar1 = np.array([4,2,9,4,5,7])
print(Ar1)
# Ar1[:2] = 0
# print(Ar1)


# Ar1[:2] = [1,4]
# print(Ar1)


# sl_ar = Ar1[2:]  #view not copy
sl_ar = Ar1[2:].copy()

sl_ar[:] = 0
print(sl_ar)
print(Ar1)




# --------------------------- Here is more details ----------------------------

a1=np.array([2,3,4,5,6])

# a2=a1          #Aliasing same addr same value

# a2=a1.view()   #diffrenet addr same valu
a1[2]=9        #Shallow copy both are dependent each other

a2=a1.copy()   #Deep  copy not dependent each other

print(a1)
print(a2)
print(id(a1))
print(id(a2))


# 13 conditional Selection

arry = np.arange(1,21)
print(arry)
print(type(arry))

print(arry>5)
elon = arry>7
print(arry[elon]) 

print(arry[arry%2==0])

print(arry[arry%5==0])






# 14 Operation with Numpy array

# arry1 = np.arange(1,10)
# print(arry1)
# print(arry1 + 5)
# print(arry1 * 5)
# print(arry1 ** 2)
# print(arry1 - 5)

# arry1 = np.arange(1,10).reshape(3,3)
# print(arry1)
# print(arry1 + 5)
# print(arry1 * 5)
# print(arry1 ** 2)
# print(arry1 - 5)

# print(1/0)
# print(arry1 / 0)

# array1 = np.array([5,6,7,8]) 
# array2 = np.array([1,2,3,4])
# # array2 = np.array([1,2,3])  # dimension must be same


# print(array1 + array2) 
# print(array1 - array2) 
# print(array1 * array2) 
# print(array1 / array2) 
# print(array1 ** array2) 



np.random.seed(123)
array11 = np.random.randint(1,50,9).reshape((3,3))
array22 = np.random.randint(20,35,9).reshape((3,3))
print(array11)
print(array22)

print(array11 + array22) 
print(array11- array22) 
print(array11 * array22) 
print(array11 / array22) 

print(array11.dot(array22))   # matrix Multiplication



array111 = np.array([34,54,21,43,78,98,33,56])
print(array111)
print(np.max(array111))
print(np.min(array111))
print(np.argmax(array111))
print(np.argmin(array111))
print(np.sqrt(array111))
print((array11)**2)

print(np.exp(array111))

# oylar number 2.71828**value
print(2.71828 ** 34)
print(np.sin(array111))
print(np.cos(array111))
print(np.tan(array111))

print(np.linspace(1,15,20))






# Numpy Axis

np.random.seed(123)
mat = np.random.randint(1,11,9).reshape(3,3)
print(mat)
print(np.sum(mat))
print(mat.sum())

print(np.max(mat))
print(mat.max())

print(np.min(mat))
print(mat.min())


# row = 1    ,  column = 0

print(np.min(mat , axis = 1))  # Row wise minimum  [3 2 1]

# 1st value =>minimum value of 1st row
# 2nd value =>minimum value of 2nd row
# 3rd value =>minimum value of 3rd row
# axis = 1 means row wise
# axis = 0 means column wise

print(np.max(mat , axis = 0))

# Cumalative sum()
print(np.cumsum(mat))
print(np.cumsum(mat , axis = 1))
print(np.cumsum(mat , axis = 0))




# sort along the first axis

a = np.array([[12, 15], [10, 1]])
arr1 = np.sort(a, axis = 0)        
print ("Along first axis : \n", arr1)        
 
 
# sort along the last axis
a = np.array([[10, 15], [12, 1]])
print(a)
arr2 = np.sort(a, axis = -1)        
print ("\nAlong first axis : \n", arr2)
 
arr2 = np.sort(a, axis = 1)        
print ("\nAlong first axis : \n", arr2)
 
 
a = np.array([[12, 15], [10, 1]])
arr1 = np.sort(a, axis = None)        
print ("\nAlong none axis : \n", arr1)


# Numpy array created
a = np.array([9, 3, 1, 7, 4, 3, 6])
 
# unsorted array print
print('Original array:\n', a)
 
# Sort array indices
print(np.sort(a))
b = np.argsort(a)
print('Sorted indices of original array->', b)
 





# Shuffle and Unique

np.random.seed(123)
matr = np.random.randint(1,15,15)
print(matr)
np.random.shuffle(matr)
print(matr)
np.unique(matr)
np.unique(matr).size

np.unique(matr , return_index=True  ,return_counts=True)

# First line --> return unique array
# Second line --> return unique array value Indexes
# Third line --> return how many times unique array value occurance








# hstack() an vstack()
np.random.seed(123)
matrix1 = np.random.randint(1,15,9).reshape(3,3)
matrix2 = np.random.randint(1,30,9).reshape(3,3)

print(matrix1)
print(matrix2)

print(np.vstack((matrix1,matrix2)))  # vertically concate 2 array # khara add
print(np.hstack((matrix1,matrix2)))  # horizently concate 2 array # sojasuji add



matrix11 = np.random.randint(1,15,4)
matrix22 = np.random.randint(1,30,4)

print(matrix11)
print(matrix22)

print(np.vstack((matrix11,matrix22)))  # vertically concate 2 array # khara add
print(np.hstack((matrix11,matrix22)))






# Exercise
import numpy as np
# Create an Array using array function
arr = np.array([1,2,3])
arr

# Create an Array containing numbers from 20 to 40 
arr2 = np.arange(20,41)
arr2

# Create an array which contain 10 elements and every element is 5
fives = np.ones(10)*5
fives

# create a 1-d array and then convert it into 3-d array
arr3 = np.random.randint(1,50,24).reshape(3,4,2)
arr3

# Create 2-d array which contains random 25 numbers between 0 and 1
arr4 = np.random.rand(4,5)
arr4


# create array containing 20 random integer then replace every even number with -1
# Example -
# array --- > [44,55,12,6,3]
# ouput ----> [-1,55, -1,-1,3

np.random.seed(123)
arr5 = np.random.randint(1,50,20)
arr5[arr5 %2 == 0] = -1
arr5


# You have a matrix
# [[5 , 10, 15, 20, 25], [30, 35, 40, 45, 50], [55, 60, 65, 70, 75], [80, 85, 90, 95, 100]]

# Extract [30,35,40] [55, 60, 65]

matrix = np.array([[5 , 10, 15, 20, 25],
                   [30, 35, 40, 45, 50],
                   [55, 60, 65, 70, 75],
                   [80, 85, 90, 95, 100]])
matrix[1:3,0:3 ]



# Concatenate two 1-d array
arr7 = np.array([1,2,3])
arr8 = np.array([4,5,6])
np.hstack((arr7,arr8))


# Stack 2-d matrix horizontally and vertically

matrix2 = np.random.randint(1,10,9).reshape(3,3)
matrix3 = np.random.randint(10,20,9).reshape(3,3)

matrix2
matrix3
np.vstack((matrix2, matrix3))










