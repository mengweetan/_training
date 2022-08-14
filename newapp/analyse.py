import pandas as pd

df = pd.read_csv('_data.csv')
# print(df)
# #
# print(df.shape)
# print(df.describe())
# print(df.head(10))
# print(df.tail(5))
# print(df['month'])
# print(df.loc[9])
# newdf = f['month'] = '02'
#
# # print(df['month'])
# #
# df['by-year'] = df.apply(lambda row: row['month'][:4], axis=1)
df['by-month'] = df.apply(lambda row: row['month'][5:], axis=1)
# # print(df.head(10))
#
# print(df.groupby(["by-year"]).count())
# print(df.groupby(["by-year"]).mean())
#
# print(df.groupby(["by-month"]).count())
# print(df.groupby(["by-month"]).mean())

gen_df = df.groupby(["by-month"]).mean()

result = gen_df.to_json()
print(result)
