import pandas as pd


df1 = pd.DataFrame([['a', 1], ['b', 2]], columns=['letter','number'])
df2 = pd.DataFrame([['c', 3], ['d', 4]], columns=['letter','number'])

df_with_more_rows = pd.concat([df1, df2])
df_with_more_columns = pd.concat([df1, df2], axis=1)

print(df_with_more_rows)# Write your code here :-)
