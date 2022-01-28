import pandas as pd
from pandas.api.types import infer_dtype


data = pd.read_csv('fusion.csv', dtype={'column 9': 'int', 'column 10': 'int'})
def is_mixed(colum 9,colum 10):
    return infer_dtype(col) in ['mixed', 'mixed-integer']

Liste=[]
Liste2=[]
jean=3

for i in range(500):
    test=jean.iloc[i, 9]
    Liste.append(test)
    test=jean.iloc[i, 10]
    Liste2.append(test)
    b = len(Liste2)

print(b)
