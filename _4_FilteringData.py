import pandas as pd

bios = pd.read_csv("./data/bios.csv")

biosinfo = bios.info()
# filter bios data with height > 215 | NOC == United States | columns filtered with name, height_cm, NOC
dataframe2 = bios.loc[(bios["height_cm"] > 215) & (bios["NOC"] == "United States"), ["name", "height_cm", "NOC"]] 

#

print(dataframe2)