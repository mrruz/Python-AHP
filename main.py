import pandas
li = ['Price or Cost', 'Storage Space', 'Camera', 'Looks']

df = pandas.DataFrame(1.0, columns=li, index=li)

z = len(li)
col = 0
row = 0

## Pair-wise comparison
while row < z:
    while col < z:    
        if col != row:
            print('Comparing\n A: {}\nTO\n B: {}'.format(li[row], li[col]))
##            print('(1 = A is greater | 2 = Both are equal | 3 = B is greater)')
            answer = float(input('ENTER: '))
            df[li[col]][li[row]] = answer
            df[li[row]][li[col]] = 1 / answer
        col += 1   
    row += 1
    col = row

df2 = df.copy()

df2.loc[:, li] = df2.loc[:, li].div(df2.sum(axis=0), axis=1)
df2['Criteria Weight'] = df2.mean(axis=1)
df2 = df2['Criteria Weight']

df = pandas.DataFrame(df.values*df2.values, columns=df.columns, index=df.index)
df['Weighted Sum Value'] = df.sum(axis=1)
df = df.join(df2)
del df2

df.to_csv('output.csv')
