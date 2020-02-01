import pandas as pd

df = pd.read_excel('trekking1.xlsx')
# print(len(df))
# print(df.columns)
# print(df[df['ККал на 100'].isna()])
print(df.sort_values(['ККал на 100', 'Unnamed: 0'], ascending=[False,True])['Unnamed: 0'].\
      to_csv(sep='\t', index=False, quotechar="'"))