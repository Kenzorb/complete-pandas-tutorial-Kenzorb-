import pandas as pd

coffee = pd.read_csv("./warmup-data/coffee.csv")

originaldataframe = coffee
dataframe1 = coffee.sample(10)
dataframe2 = coffee.loc[[0, 1, 5]]
dataframe3 = coffee.loc[0: 3]
dataframe4 = coffee.loc[0: 3, ["Day", "Units Sold"]]
dataframe5 = coffee.iloc[0:3, [0,2]]

coffee.loc[1:3, "Units Sold"] = 10
dataframe6 = coffee.head()

dataframe7 = coffee.at[0, "Units Sold"]
dataframe8 = coffee.iat[0, 2]

dataframe9 = coffee["Day"]
dataframe10 = coffee.sort_values("Units Sold")
dataframe11 = coffee.sort_values("Units Sold", ascending=False)
dataframe12 = coffee.sort_values(["Units Sold", "Coffee Type"], ascending=False)

testcase = 3
if testcase == 1:
    for index, row in coffee.iterrows():
        print(index)
        print(row)
        print("\n\n\n")

if testcase == 2:
    for index, row in coffee.iterrows():
        print(index)
        print(row["Units Sold"])
        print("\n\n\n")

if testcase == 3:
    print(originaldataframe)
    print("-----------")
    print(dataframe12)