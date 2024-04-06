"""| Задание 44 |
| --- |
| В ячейке ниже представлен код генерирующий DataFrame, 
которая состоит всего из 1 столбца.
 Ваша задача перевести его в one hot вид. 
 Сможете ли вы это сделать без get_dummies?
"""

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()




one_hot_encoded = pd.get_dummies(data, columns=['whoAmI'])
print(one_hot_encoded.head())


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

unik = data['whoAmI'].unique()
for new in unik:
    data[new] = (data['whoAmI'] == new).astype(int)
data.drop(columns=['whoAmI'], inplace=True)
data.head()

