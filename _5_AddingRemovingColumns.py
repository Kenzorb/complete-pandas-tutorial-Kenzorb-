import pandas as pd
import numpy as np

coffee = pd.read_csv("./warmup-data/coffee.csv")

dataframe1 = coffee

# Added price column
coffee["price"] = 4.99
dataframe2 = coffee

# Added new price for different coffee types
coffee["new_price"] = np.where(coffee["Coffee Type"]=="Espresso", 3.99, 5.99)
dataframe3 = coffee.head()

# Deleting a column. Remove the old price
coffee = coffee.drop(columns=["price"])
dataframe4 = coffee.head()

# Duplicating a dataframe
dup_coffee = coffee.copy()  # Copy() is needed to create a copy. If not dup_coffee will refer to the same memoery as coffee
dup_coffee["Ingredient"] = np.where(coffee["Coffee Type"]=="Espresso", r"100% Espresso", r"33.3% Espresso, 66.6% Milk, Little Foam")
dataframe5 = dup_coffee

# Adding new revenue column
coffee["revenue"] = coffee["Units Sold"] * coffee["new_price"]
dataframe6 = coffee.head()

# Renaming new_price column
coffee = coffee.rename(columns={"new_price":"price"})
dataframe7 = coffee.head()


print(dataframe7)