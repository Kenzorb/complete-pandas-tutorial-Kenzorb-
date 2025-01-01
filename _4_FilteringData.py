import pandas as pd

bios = pd.read_csv("./data/bios.csv")

biosinfo = bios.info()
# filter: height > 215 | NOC == United States | columns filtered with name, height_cm, NOC
dataframe2 = bios.loc[(bios["height_cm"] > 215) & (bios["NOC"] == "United States"), ["name", "height_cm", "NOC"]] 

# filter: name contains 'keith'
dataframe3 = bios.loc[(bios["name"].str.contains(r"John | chua$", case=False)), ["name", "height_cm"]]
#       .str.contains() is a method form the pandas library
#       " | " and "$" is a RegEx(Regular Expression)
#       need to use raw string for '$'

dataframe4 = bios.loc[(bios["born_country"].isin(["USA", "FRA"])) & bios["name"].str.contains(r"^keith", case=False), ["name", "born_country"]]

print(dataframe4.tail(20))