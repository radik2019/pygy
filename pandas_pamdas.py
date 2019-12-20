

a = [[0 for i in range(10)] for i in range(10)]
a[1][2] = 1
a[1][3] = 1
a[1][4] = 1
a[3][2] = 1
a[4][2] = 1
a[4][3] = 1
a[7][2] = 1
a[7][3] = 1
a[0][6] = 1
a[0][6] = 1
a[0][6] = 1
a[1][2] = 1
a[1][3] = 1
a[1][4] = 1
a[3][2] = 1
a[4][2] = 1
a[4][3] = 1
a[0][6] = 1
a[1][6] = 1
a[2][6] = 1
a[3][6] = 1
a[4][6] = 1
a,b,c,d,e,f,g,h,i,h = 0,1,2,3,4,5,6,7,8,9



import pandas as pd
df = pd.DataFrame({'paese':['Italia','Francia','Germania'], 'macchine':['ferrari','renault','mercedes'], 'lingua':['italiana','francese','tedesca'], 'YEAR':[1982,1978,1983]})

print(df)
df = df.rename({'paese':'COUNTRY','macchine':'CAR', 'lingua':'LANG'},axis='columns')
#pd.show_versions()

print()
print(df)
print()
df = df.add_prefix('ex_')
print(df)
# *******************************"*"
# selseziona il tipo di datil
print(df.select_dtypes(include='number').head())
df.to_csv('table.csv')



