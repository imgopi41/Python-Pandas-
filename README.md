**Python Pandas**

Pandas is an open source Python package that is most widely used for data science/data analysis and machine learning tasks. 
It is built on top of another package named Numpy, which provides support for multi-dimensional arrays. 
As one of the most popular data wrangling packages, Pandas works well with many other data science modules inside the Python ecosystem,
and is typically included in every Python distribution, from those that come with your operating system to commercial 
vendor distributions like ActiveState’s ActivePython. 

**DataFrame**

Pandas DataFrame is a 2-dimensional labeled data structure like any table with rows and columns. The size and values of the dataframe are mutable,
i.e., can be modified. It is the most commonly used pandas object. Pandas DataFrame can be created in multiple ways. 
Let’s discuss different ways to create a DataFrame one by one.

DataFrame() function is used to create a dataframe in Pandas. The syntax of creating dataframe is:

pandas.DataFrame(data, index, columns)

**data:** It is a dataset from which dataframe is to be created. It can be list, dictionary, scalar value, series, ndarrays, etc.

**index:** It is optional, by default the index of the dataframe starts from 0 and ends at the last data value(n-1). It defines the row label explicitly.

**columns:** This parameter is used to provide column names in the dataframe. If the column name is not defined by default, it will take a value from 0 to n-1.


**Pandas DataFrame can be Created 6 different Ways:**


**Method 1:** Creating  Dataframe from Lists

**Method 2:** Creating Pandas DataFrame from lists of lists.

**Method 3:** Creating DataFrame from dict of narray/lists.

**Method 4:** Creating Dataframe from list of dicts.

**Method 5:** Creating DataFrame using zip() function.




