import pandas as pd

bios = pd.read_csv("./data/bios.csv")

dataframe1 = bios.head()

# Getting the first name
bios_new = bios.copy()
bios_new["first_name"] = bios_new["name"].str.split(" ").str[0]
dataframe2 = bios_new

# Getting the birth year
bios_new["born_datetime"] = pd.to_datetime(bios_new["born_date"])   # recommended to convert from 'object' datatype to 'datetime64' datatype to easily work with the datetime values
bios_new["born_year"] = bios_new["born_datetime"].dt.year       #access dt(datetime) and year
dataframe3 = bios_new[["first_name", "born_year"]]      #filter the columns to "first_name" and "born_year"

# Saving the new bios under data
bios_new.to_csv("./data/bios_new.csv", index=False)

# Classifying people into height categories. Adds a new column height_category to classify peoples heights
# The .apply() method in Pandas is used to apply a function along a specific axis (either rows or columns) of a DataFrame
bios['height_category'] = bios["height_cm"].apply(lambda x: "Short" if x < 165 else ("Average" if x < 185 else "Tall"))
dataframe4 = bios.head()

# Classifying people into weight classes using functions instead of lambda. Functions are not optimized for pandas
def categorize_athlete(row):
    if row["height_cm"] < 175 and row["weight_kg"] < 70:
        return "Lightweight"
    elif row["height_cm"] < 185 and row["weight_kg"] < 80:
        return "Middleweight"
    else:
        return "Heavyweight"
    
bios["Weight_Category"] = bios.apply(categorize_athlete, axis=1)
dataframe5 = bios.head()


print(dataframe5)