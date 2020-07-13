'''
Pandas series 
Jana Rasras
'''


import pandas as pd 
import numpy as np

groceries = pd.Series(data=[3, 6,'yes', 'no'], index = ['egg', 'apple', 'milk', 'bread'])

print(groceries)

print(groceries.shape)

print(groceries.ndim)

print(groceries.size)
print(groceries.values)
print(groceries.index)

print('banana' in groceries)
print('bread' in groceries)

# P02 :Accessing and Deleting Elements in Pandas Series
print(groceries['egg'])
print(groceries[-1])
print('Do we need milk and bread:\n', groceries.iloc[[2, 3]]) 

# P03: Arithmetic Operations on Pandas Series
 
fruits = pd.Series(data=[1,3, 4, 5], index= ['apple', 'banana', 'mango', 'lemon'])

print(fruits+2)

print(np.power(fruits,2))

print(fruits['banana']+2)
print(fruits.iloc[0]-2)

# P04: Creating Pandas DataFrames
 
items = {'Modar': pd.Series(data=[100, 500 , 2], index = ['book', 'mac', 'bike']),
        'Alice': pd.Series(data=[40, 60, 70,77], index=['bike', 'book','football', 'cd'])}

print(type(items))
shopping_carts = pd.DataFrame(items)
print(shopping_carts)

print('shopping_carts has shape:', shopping_carts.shape)
print('shopping_carts has dimension:', shopping_carts.ndim)
print('shopping_carts has a total of:', shopping_carts.size, 'elements')
print()
print('The data in shopping_carts is:\n', shopping_carts.values)
print()
print('The row index in shopping_carts is:', shopping_carts.index)
print()
print('The column index in shopping_carts is:', shopping_carts.columns)

# P06 Dealing with NAN
s = shopping_carts.isnull()
X = shopping_carts.isnull().sum().sum()
print(s)
print(X)

print(shopping_carts.count())
a = shopping_carts.dropna(axis=0)
print(a)

print(shopping_carts.fillna(0))

print(shopping_carts.fillna(method = 'ffill', axis = 0))

#Google_stock = pd.read_csv('./GOOG.csv')


