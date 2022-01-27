import pandas as pd



jean = pd.read_csv('fusion.csv', index_col=False)
Liste=[]
Liste2=[]

for i in range(500):
    test=jean.iloc[i, 9]
    Liste.append(test)
    test=jean.iloc[i, 10]
    Liste2.append(test)
    b = len(Liste2)

print(b)
