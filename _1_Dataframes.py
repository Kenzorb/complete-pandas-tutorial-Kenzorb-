import pandas as pd

dataset3 = {
    "cars": ["BMW", "Volvo", "Ford"],
    "passings": [3, 7, 2]
}

#Dataframes are tables with extra functionality.
df1 = pd.DataFrame([[1,2,3], [4,5,6], [7,8,9]])
df2 = pd.DataFrame([[1,2,3], [4,5,6], [7,8,9]], columns=["A", "B", "C"])
df3 = pd.DataFrame(dataset3)
df4 = pd.DataFrame([[1,2,3], [4,5,6], [7,8,9]], columns=["A", "B", "C"], index=["X", "Y", "Z"])

dataframe1 = df1.head()     # head method returns a specific number of rows from the top. Displays only first 5 rows if not specified.
dataframe2 = df2.head()
dataframe3 = df3.head()
dataframe4 = df2.head(1)    # returns 1 row
dataframe5 = df2.tail(2)    # tail(2) returns 2 rows from the bottom.
dataframe6 = df2.columns    # If I want to see the column headers
dataframe7 = df2.index    # If I want to see the row index
dataframe8 = df2.index.tolist()
dataframe9 = df4.head()
dataframe10 = df4.describe()

print("\n1------------\n")
print(dataframe1)
print("\n2------------\n")
print(dataframe2)
print("\n3------------\n")
print(dataframe3)
print("\n4------------\n")
print(dataframe4)
print("\n5------------\n")
print(dataframe5)
print("\n6------------\n")
print(dataframe6)
print("\n7------------\n")
print(dataframe7)
print("\n8------------\n")
print(dataframe8)
print("\n9------------\n")
print(dataframe9)
print("\n10------------\n")
print(dataframe10)
print("\n.shape------------\n")
print(df2.shape)