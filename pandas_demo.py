import pandas as pd

df=pd.read_csv("daataset.csv")
# print(df.info())
# print(df.shape)
# print(df["country"])
# print(df.loc[0])
# print(df.loc[[7,8]])
# print(df.loc[list(range(100))])
# print(df.head(10))
# print(df.tail(10))
# print(df.columns)
# print(df.keys())
# print(df["country"].unique())
# print(df[["country","year"]])
# print(df["country"].head())
# print(df["country"].tail())
# print(df["country"].value_counts())


# df.rename({"country":"Country_Name","population":"Population_count"},axis=1,inplace=True)
# print(df["Country_Name"])
# df.drop("year",axis=1,inplace=True)
# print(df)
# df["year"]+=7
# print(df)


a={"country":"Afganisthan","year":2025}
y=pd.DataFrame([a])
print(pd.concat([df,y],ignore_index=True))