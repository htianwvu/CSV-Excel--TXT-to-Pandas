### learning pandas
### series and dataframe

### Series

import pandas as pd

# series
s1 = pd.Series(['a','b','c','d'])
print(s1)

s2 = pd.Series(['a','b','c','d'],index = [1,2,3,4])
print(s2)

# input dictionary key is index, value is data

s3 = pd.Series({1:'a',2:'b',3:'c',4:'d'})
print(s3)

print(s1.index)
print(s2.index)

print(s1.values)
print(s2.values)


## dataframe

df1 = pd.DataFrame(['a','b','c','d'])
print(df1)
df2 = pd.DataFrame([['a','A'],['b','B'], ['c','C'],['d','D']])
print(df2)

df3 = pd.DataFrame([['a','A'],['b','B'], ['c','C'],['d','D']], 
                   columns = ['big','small'], index = ["yi","er","san","si"])
print(df3)

print(df3.columns)
print(df3.index)


