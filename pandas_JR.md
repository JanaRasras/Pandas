


__Pandas :)__

- We are on to a Python library, Pandas, a data manipulation and analysis tool.

---


## Introduction to Pandas

**Pandas** is a package for data manipulation and analysis in Python. The name Pandas is
derived from the econometrics term Panel Data. Pandas incorporates two additional data
structures into Python, namely **Pandas Series** and **Pandas DataFrame**. These data
structures allow us to work with labeled and relational data in an easy and intuitive
manner. These lessons are intended as a basic overview of Pandas and introduces some
of its most important features.



In this tutorial you will learn:

+ How to import Pandas
+ How to create Pandas Series and DataFrames  using various methods
+ How to access and change elements in Series and DataFrames
+ How to perform arithmetic operations on Series
+ How to load data into a DataFrame
+ How to deal with Not a Number (NaN) values

The following tutorial assumes that you are already familiar with NumPy. Therefore, to avoid being repetitive I will omit a lot of
details about NumPy. Consequently, if you are not familiar with NumPy, I suggest you go over it first. 

---
## Downloading Pandas

Pandas is included with **Anaconda**. If you don't already have Anaconda installed on your
computer, please refer to the Anaconda section to get clear instructions on how to install Anaconda on your PC or Mac.

## Pandas Versions
As with many Python packages, Pandas is updated from time to time. The following
tutorial was created using Pandas version 0.22. You can check which version of Pandas
you have by typing `!conda list pandas` in your Jupyter notebook or by typing conda list
pandas in the Anaconda prompt. If you have another version of Pandas installed in your
computer, you can update your version by typing `conda install pandas=0.22` in the
Anaconda prompt. As newer versions of Pandas are released, some functions may
become obsolete or replaced, so make sure you have the correct Pandas version before
running the code. This will guarantee your code will run smoothly.

## Pandas Documentation
Pandas is remarkable data analysis library and it has many functions and features. In
these introductory lessons we will only scratch the surface of what Pandas can do. If you
want to learn more about Pandas, make sure you check out the Pandas Documentation:
[Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/
)

TODO: explain how to read the doc.

---

## Why Use Pandas?
The recent success of machine learning algorithms is partly due to the huge amounts of
data that we have available to train our algorithms on. However, when it comes to data,
quantity is not the only thing that matters, the quality of your data is just as important. It
often happens that large datasets don’t come ready to be fed into your learning
algorithms. More often than not, large datasets will often have missing values, outliers,
incorrect values, etc… Having data with a lot of missing or bad values, for example, is not
going to allow your machine learning algorithms to perform well. Therefore, one very
important step in machine learning is to look at your data frst and make sure it is well
suited for your training algorithm by doing some basic data analysis. This is where Pandas
come in. Pandas Series and DataFrames are designed for fast data analysis and
manipulation, as well as being fexible and easy to use. Below are just a few features that
makes Pandas an excellent package for data analysis:

+ Allows the use of labels for rows and columns

+ Can calculate rolling statistics on time series data

+ Easy handling of NaN values
+ Is able to load data of different formats into DataFrames
+ Can join and merge different datasets together
+ It integrates with NumPy and Matplotlib

For these and other reasons, Pandas DataFrames have become one of the most
commonly used Pandas object for data analysis in Python.


---

## Creating Pandas Series
Pandas is  a powerful tool for data analysis and manipulation. It is a package that built up on NumPy.

Let's start learning about Pandas Series.

Inline `code`

Indented code

     import pandas as pd
     # We create a Pandas Series that stores a grocery list
     groceries = pd.Series(data = [30, 6, 'Yes', 'No'], index = ['eggs', 'apples', 'milk', 'bread'])
     # We display the Groceries Pandas Series
    groceries

When importing pandas, use the standard alias *pd*

To access the series we type pd.Series with capital S.

A panda series is  a 1D array that can hold many data types.

You can assign an index label to each element in the panda series.

Indented code

    # We print some information about Groceries
    print('Groceries has shape:', groceries.shape)
    print('Groceries has dimension:', groceries.ndim)
    print('Groceries has a total of', groceries.size, 'elements')
    
    # We print the index and data of Groceries
    print('The data in Groceries is:', groceries.values)
    print('The index of Groceries is:', groceries.index)

    # We check whether bananas is a food item (an index) in Groceries
    x = 'bananas' in groceries

    # We check whether bread is a food item (an index) in Groceries
    y = 'bread' in groceries

    # We print the results
    print('Is bananas an index label in Groceries:', x)
    print('Is bread an index label in Groceries:', y)


Just Like NumPy array, Pandas Series have attributes that allows to get data from them in an easy way.

`shape` gives the sizes of each dimension of the data.

`ndim` gives us the dimention of the data.

`size` gives us the total number of values in the array.
`index` gives us the index labels of the series object.
`values` gives us the data in the series object.
`in` checks if an element in the data series.

------
## Accessing and Deleting Elements in Pandas Series

    # We access elements in Groceries using index labels:

    # We use a single index label
    print('How many eggs do we need to buy:', groceries['eggs'])
    print()

    # we can access multiple index labels
    print('Do we need milk and bread:\n', groceries[['milk', 'bread']]) 
    print()

    # we use loc to access multiple index labels
    print('How many eggs and apples do we need to buy:\n',                                     groceries.loc[['eggs', 'apples']]) 
    print()

    # We access elements in Groceries using numerical indices:

    # we use multiple numerical indices
    print('How many eggs and apples do we need to buy:\n',  groceries[[0, 1]]) 
    print()

    # We use a negative numerical index
    print('Do we need bread:\n', groceries[[-1]]) 
    print()

    # We use a single numerical index
    print('How many eggs do we need to buy:', groceries[0]) 
    print()
    # we use iloc to access multiple numerical indices
    print('Do we need milk and bread:\n', groceries.iloc[[2, 3]])

---
 
## Arithmetic Operations on Pandas Series

    # We create a Pandas Series that stores a grocery list of just fruits
    fruits= pd.Series(data = [10, 6, 3,], index = ['apples', 'oranges', 'bananas'])

    # We display the fruits Pandas Series
fruits


    # We print fruits for reference
    print('Original grocery list of fruits:\n ', fruits)

    # We perform basic element-wise operations using arithmetic symbols
    print()
    print('fruits + 2:\n', fruits + 2) # We add 2 to each item in fruits
    print()
    print('fruits - 2:\n', fruits - 2) # We subtract 2 to each item in     
    fruits
    print()
    print('fruits * 2:\n', fruits * 2) # We multiply each item in fruits by 2 
    print()
    print('fruits / 2:\n', fruits / 2) # We divide each item in fruits by 2
    print()


    # We import NumPy as np to be able to use the mathematical functions
    import numpy as np

    # We print fruits for reference
    print('Original grocery list of fruits:\n', fruits)

    # We apply different mathematical functions to all elements of fruits
    print()
    print('EXP(X) = \n', np.exp(fruits))
    print() 
    print('SQRT(X) =\n', np.sqrt(fruits))
    print()
    print('POW(X,2) =\n',np.power(fruits,2)) # We raise all elements of     fruits to the power of 2



    # We print fruits for reference
    print('Original grocery list of fruits:\n ', fruits)
    print()

    # We add 2 only to the bananas
    print('Amount of bananas + 2 = ', fruits['bananas'] + 2)
    print()

    # We subtract 2 from apples
    print('Amount of apples - 2 = ', fruits.iloc[0] - 2)
    print()

    # We multiply apples and oranges by 2
    print('We double the amount of apples and oranges:\n',         
    fruits[['apples', 'oranges']] * 2)
    print()

    # We divide apples and oranges by 2
    print('We half the amount of apples and oranges:\n',     fruits.loc[['apples', 'oranges']] / 2)


    # We multiply our grocery list by 2
    groceries * 2
----

## Pandas DataFrames



        # We import Pandas as pd into Python
        import pandas as pd

        # We create a dictionary of Pandas Series 
        items = {'Bob' : pd.Series(data = [245, 25, 55], index = ['bike', 'pants', 'watch']),
                'Alice' : pd.Series(data = [40, 110, 500, 45], index = ['book', 'glasses', 'bike', 'pants'])}

        # We print the type of items to see that it is a dictionary
        print(type(items))



        # We create a Pandas DataFrame by passing it a dictionary of Pandas Series
        shopping_carts = pd.DataFrame(items)

        # We display the DataFrame
        shopping_carts


        # We create a dictionary of Pandas Series without indexes
        data = {'Bob' : pd.Series([245, 25, 55]),
                'Alice' : pd.Series([40, 110, 500, 45])}

        # We create a DataFrame
        df = pd.DataFrame(data)

        # We display the DataFrame
        df


        # We print some information about shopping_carts
        print('shopping_carts has shape:', shopping_carts.shape)
        print('shopping_carts has dimension:', shopping_carts.ndim)
        print('shopping_carts has a total of:', shopping_carts.size, 'elements')
        print()
        print('The data in shopping_carts is:\n', shopping_carts.values)
        print()
        print('The row index in shopping_carts is:', shopping_carts.index)
        print()
        print('The column index in shopping_carts is:', shopping_carts.columns)



        # We Create a DataFrame that only has Bob's data
        bob_shopping_cart = pd.DataFrame(items, columns=['Bob'])

        # We display bob_shopping_cart
        bob_shopping_cart



        # We Create a DataFrame that only has selected items for both Alice and Bob
        sel_shopping_cart = pd.DataFrame(items, index = ['pants', 'book'])

        # We display sel_shopping_cart
        sel_shopping_cart


        # We Create a DataFrame that only has selected items for Alice
        alice_sel_shopping_cart = pd.DataFrame(items, index = ['glasses', 'bike'], columns = ['Alice'])

        # We display alice_sel_shopping_cart
        alice_sel_shopping_cart


        # We create a dictionary of lists (arrays)
        data = {'Integers' : [1,2,3],
                'Floats' : [4.5, 8.2, 9.6]}

        # We create a DataFrame 
        df = pd.DataFrame(data)

        # We display the DataFrame
        df

        # We create a dictionary of lists (arrays)
        data = {'Integers' : [1,2,3],
                'Floats' : [4.5, 8.2, 9.6]}

        # We create a DataFrame and provide the row index
        df = pd.DataFrame(data, index = ['label 1', 'label 2', 'label 3'])

        # We display the DataFrame
        df


        # We create a list of Python dictionaries
        items2 = [{'bikes': 20, 'pants': 30, 'watches': 35}, 
                {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5}]

        # We create a DataFrame 
        store_items = pd.DataFrame(items2)

        # We display the DataFrame
        store_items


        # We create a list of Python dictionaries
        items2 = [{'bikes': 20, 'pants': 30, 'watches': 35}, 
                {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5}]

        # We create a DataFrame  and provide the row index
        store_items = pd.DataFrame(items2, index = ['store 1', 'store 2'])

        # We display the DataFrame
        store_items
---
## Accessing Elements in Pandas DataFrames


        # We print the store_items DataFrame
        print(store_items)

        # We access rows, columns and elements using labels
        print()
        print('How many bikes are in each store:\n', store_items[['bikes']])
        print()
        print('How many bikes and pants are in each store:\n', store_items[['bikes', 'pants']])
        print()
        print('What items are in Store 1:\n', store_items.loc[['store 1']])
        print()
        print('How many bikes are in Store 2:', store_items['bikes']['store 2'])


        # We add a new column named shirts to our store_items DataFrame indicating the number of
        # shirts in stock at each store. We will put 15 shirts in store 1 and 2 shirts in store 2
        store_items['shirts'] = [15,2]

        # We display the modified DataFrame
        store_items


        # We make a new column called suits by adding the number of shirts and pants
        store_items['suits'] = store_items['pants'] + store_items['shirts']

        # We display the modified DataFrame
        store_items


        # We create a dictionary from a list of Python dictionaries that will number of items at the new store
        new_items = [{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4}]

        # We create new DataFrame with the new_items and provide and index labeled store 3
        new_store = pd.DataFrame(new_items, index = ['store 3'])

        # We display the items at the new store
        new_store


        # We append store 3 to our store_items DataFrame
        store_items = store_items.append(new_store)

        # We display the modified DataFrame
        store_items


        # We add a new column using data from particular rows in the watches column
        store_items['new watches'] = store_items['watches'][1:]

        # We display the modified DataFrame
        store_items


        # We insert a new column with label shoes right before the column with numerical index 4
        store_items.insert(4, 'shoes', [8,5,0])

        # we display the modified DataFrame
        store_items


        # We remove the new watches column
        store_items.pop('new watches')

        # we display the modified DataFrame
        store_items


        # We remove the watches and shoes columns
        store_items = store_items.drop(['watches', 'shoes'], axis = 1)

        # we display the modified DataFrame
        store_items


        # We remove the store 2 and store 1 rows
        store_items = store_items.drop(['store 2', 'store 1'], axis = 0)

        # we display the modified DataFrame
        store_items


        # We change the column label bikes to hats
        store_items = store_items.rename(columns = {'bikes': 'hats'})

        # we display the modified DataFrame
        store_items


        # We change the row label from store 3 to last store
        store_items = store_items.rename(index = {'store 3': 'last store'})

        # we display the modified DataFrame
        store_items


        # We change the row index to be the data in the pants column
        store_items = store_items.set_index('pants')

        # we display the modified DataFrame
        store_items

## TO Be Continued..

