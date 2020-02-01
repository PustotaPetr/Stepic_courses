import pandas as pd
import math

sprav, day_norm = pd.read_excel('trekking2.xlsx', sheet_name=[0,1] ).values()
sprav.columns = ['name', 'kkal', 'protein', 'fat', 'carbo']
sprav.fillna(value=0, inplace=True)
day_norm = day_norm.merge(sprav, how='left', left_on='Продукт', right_on='name')
for col in sprav.columns[1:]:
    day_norm['day_'+col] = day_norm[col]*day_norm['Вес в граммах']/100
print(*list(map(math.floor,day_norm[['day_'+col for col in sprav.columns[1:]]].sum(axis=0).to_list())))

