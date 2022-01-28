import pandas as pd
import pandas as pds
import numpy as np
import csv


#fusion

for i in range(1, 6):
    lecture = pds.read_csv(f"youtube-{i}.csv", header=None)
    test = lecture.drop(lecture.columns[15], axis=1)
    test.to_csv(f"youtubebis{i}.csv")
df = pd.concat(
 map(pd.read_csv, ['youtubebis1.csv', 'youtubebis2.csv', 'youtubebis3.csv', 'youtubebis4.csv', 'youtubebis5.csv', ]), ignore_index=True)
#df.to_csv("fusion.csv", index=False)




#print(df.sort_values('8', ascending=False)[:5])




#Moyenne


data = pd.read_csv('fusion.csv')
df = pd.DataFrame(data)

c=[int(i) for i in df['7'][1:]]
z=sum(c)/len(c)
z=int(z)
print("La moyenne des views est :",z)


a=[int(i) for i in df['8'][1:]]
x=sum(a)/len(a)
x=int(x)
print("La moyenne des likes est :",x)



b=[int(i) for i in df['9'][1:]]
y=sum(b)/len(b)
y=int(y)
print("La moyenne des dislikes est :",y)



#Valeur manquante

df = pd.read_csv('fusion.csv')


video = df['0']
titi=0
val = 0
print("LA VALEUR VIDEO_ID")
for vid in video:
    if vid[0]=="-":
        val += 1
print(f"Le nombre de valeur aberrante pour la colonne video_id est : {val}")
pourcen= val*100/len(video.index)
print("Voici le pourcentage des valeur aberrante", pourcen, "%")

tag = df['6']
tage = 0
print("LA VALEUR TAGS")
for ta in tag:
    if ta=="[none]":
        tage += 1
print(f"Le nombre de valeur aberrante pour la colonne video_id est : {tage}")
pourcent= tage*100/len(tag.index)
print("Voici le pourcentage des valeur aberrante pour la colonne tags est : ", pourcent, "%")