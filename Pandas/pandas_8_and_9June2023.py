"""
    Earlier, Pandas was more downloaded Python library
    Now, NumPy has overtaken it
"""

import pandas as pd
import numpy as np

a = [5, 2, 7, 4, 1]
print(type(a))
print()

pd_series = pd.Series(data=a)
print(pd_series)
print(type(pd_series))
print()

pd_series1 = pd.Series(data=[8, 11, 15, 25, 17])
print(pd_series1)
print(type(pd_series1))
print()

row_index = ["zeroth_row", "first_row", "second_row", "third_row", "fourth_row"]
row_index_series = pd.Series(data=a, index=row_index)
print(row_index_series)
print(type(row_index_series))
print()

print(pd_series * pd_series1)
print(pd_series ** pd_series1)
print(pd_series1 ** pd_series)
print()

# Creation of Dataframe
v = np.random.randn(5, 5)
print(v)
print(v.shape)
df = pd.DataFrame(data=v)
print(df)
print(type(df))
print()

df1 = pd.DataFrame(data=v, index=row_index)
print(df1)
print(type(df1))
print()

column_index = ["zeroth_column", "first_column", "second_column", "third_column", "fourth_column"]
df2 = pd.DataFrame(data=v, index=row_index, columns=column_index)
print(df2)
print(type(df2))
print()

"""
    Note - In the actual dataset, we don't have indexes named
"""

'''                  EDA - EXPLORATORY DATA ANALYSIS                       '''

print(df.head())
print()
print(df.head(2))
print()
print(df.head(4))
print()

print(df.tail())
print()
print(df.tail(2))
print()
print(df.tail(4))
print()

# Data is nothing but a combination of rows and columns in a matrix

print(df.shape)  # Prints number of rows and columns
print("\n\n\n")
print(df.info())
print("\n\n\n")

# Accessing of columns in series format
print(df2[["zeroth_column"]])
print("\n\n\n")

"""
    9th June 2023
"""

# Multiple columns of dataframe
print(df2[["zeroth_column", "first_column"]])
print("\n\n\n")

# Access rows in series using .loc() which is just location
print(df2.loc["zeroth_row"])
print("\n\n\n")

print(df2.loc["third_row"])
print("\n\n\n")

# Transpose of the above using .T
print(df2.loc["third_row"].T)
print("\n\n\n")

# Multiple rows of dataframe
print(df2.loc[["zeroth_row", "third_row"]])
print("\n\n\n")

print(df2.loc[["zeroth_row", "third_row"]].T)
print("\n\n\n")

# Accessing rows using direct index value which is .iloc() in series
print(df2.iloc[0])
print("\n\n\n")

print(df2.iloc[0].T)
print("\n\n\n")

# Accessing rows using direct index value which is .iloc() in series
print(df2.iloc[[0, 1]])
print("\n\n\n")

# When you perform slicing and dicing in .iloc() it will always display in dataframe

