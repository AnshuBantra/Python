import pandas as pd
df = pd.DataFrame(
    {
        'Data': ['A-234, E-256, D-3673', 'Q-897, R-1, S-87', 'T-90, A-308, R-45', 'S-782, D-672, Q-29']
    }
)
# df = to_df(REF("A2:A6"))
# df[['Alphabet', 'Value']] = df['Data'].str.split('-', expand=True)
# df['Value'] = df['Value'].astype(int)
# df.groupby(by='Alphabet')['Value'].sum()
df['Data'] = df['Data'].str.split(", ")
df = df.explode('Data')
df[['Alphabet', 'Value']] = df['Data'].str.split('-', expand=True)
df['Value'] = df['Value'].astype(int)
print(df.groupby(by='Alphabet')['Value'].sum())