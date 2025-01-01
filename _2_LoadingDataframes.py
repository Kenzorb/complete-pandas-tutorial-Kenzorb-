import pandas as pd

coffee = pd.read_csv("./warmup-data/coffee.csv")
results = pd.read_parquet("./data/results.parquet")
olympics = pd.read_excel("./data/olympics-data.xlsx")
olympics_data = pd.read_excel("./data/olympics-data.xlsx", sheet_name="results")    #specify a specific sheet from an excel file
bios = pd.read_csv("./data/bios.csv")

# reading from excel files takes 10x longer to load compared to parquet and feather files

dataframe1 = coffee.head()
dataframe2 = results.head()
dataframe3 = olympics.head()
dataframe4 = olympics_data.head()
dataframe5 = bios.to_parquet

print(dataframe5)