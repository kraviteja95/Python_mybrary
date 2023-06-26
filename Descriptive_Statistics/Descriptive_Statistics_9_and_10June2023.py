import pandas as pd
import numpy as np

v = np.random.randn(5, 5)
row_index = ["zeroth_row", "first_row", "second_row", "third_row", "fourth_row"]
column_index = ["zeroth_column", "first_column", "second_column", "third_column", "fourth_column"]
df = pd.DataFrame(data=v, index=row_index, columns=column_index)

# Describe function, mean, median, min, max, std
print(df.describe().T)
print(df["first_column"].median())
print("\n\n\n")

print(df["first_column"].mean())
print("\n\n\n")

print(df["first_column"].min())
print("\n\n\n")

print(df["first_column"].max())
print("\n\n\n")

"""
    10th June 2023
"""

# Create a dataframe using a dictionary
df1 = pd.DataFrame({'Customer_Id': [101, 102, 103, 104, 105], 'Laptop': ['Apple', 'Dell', 'HP', 'Acer', 'Lenovo']})
print(df1)
print("\n")
df2 = pd.DataFrame({'Customer_Id': [101, 102, 103, 104, 105], 'Brand': ['MacBook Pro', 'Alienware', 'Pavilion', 'Nitro', 'Legion']})
print(df2)
print("\n")

# Concatenate 2 DFs using .concat([]) -> By default it does row concatenation and axis=0
df_concat = pd.concat([df1, df2], axis=0)
print(df_concat)
print("\n")

# For column cocatenation , use .concat([], axis=0)
df_concat_column = pd.concat([df1, df2], axis=1)
print(df_concat_column)
print("\n")

# Merge 2 DFs using .merge() -> Outer merge - AuB in sets and Outer join in SQL
df_merge_outer = pd.merge(df1, df2, how='outer', on='Customer_Id')
print(df_merge_outer)
print("\n")

# Merge 2 DFs using .merge() -> Inner merge - AnB in sets and Outer join in SQL
df_merge_inner = pd.merge(df1, df2, how='inner', on='Customer_Id')
print(df_merge_inner)
print("\n")

df3 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df3)
print("\n")
df4 = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})
print(df4)
print("\n")

join_dfs = df3.join(df4, how='inner')
print(join_dfs)
print("\n")

join_dfs_outer = df3.join(df4, how='outer')
print(join_dfs_outer)
print("\n")

join_dfs_left = df3.join(df4, how='left')
print(join_dfs_left)
print("\n")

join_dfs_right = df3.join(df4, how='right')
print(join_dfs_right)
print("\n")
