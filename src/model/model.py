
data = pd.read_csv('U:\Documents\youtube\Sae-15-yt\data\raw\fusion.csv')
df = pd.DataFrame(data)

def ComputeMedian():
    df_median = df['8'].median()
    print("La médiane de likes est de :", int(df_median))

    df_median2 = df['9'].median()
    print("La médiane de dislikes est de :", int(df_median2))
    return False
print(ComputeMedian())

def ComputeMean():
    df_mean = df['8'].mean()
    print("La moyenne de likes est de :", int(df_mean))

    df_mean2 = df['9'].median()
    print("La moyenne de dislikes est de :", int(df_mean2))
    return False
print(ComputeMedian())
    
