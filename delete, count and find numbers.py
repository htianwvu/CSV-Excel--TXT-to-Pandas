import pandas as pd
import datetime


df = pd.read_excel(r"C:/Users/htian/Desktop/book in reading/python littlefly learning/Lesson9/Lesson9.xlsx")
df.index = ['0a','1b','2c','3d','4e']
df1 = df

print(df,"\n")
print(df.info(),'n')

#delete column
# axis = 1 means delete all colmns
print('delte名称','顶踩比例')
print(df.drop(['名称','顶踩比例'],axis=1))

# delete according columns numbers
print(df.drop(df.columns[[0,3]],axis=1))

## axis = 0 means delete all lines

print(df.drop(['0a','2c'],axis=0))
print(df.drop(df.index[[0,2]],axis=0))


################################################
# count

print(df['顶踩比例'].value_counts())
print(df['顶踩比例'].value_counts(normalize=True))

############################################
# obtain the only number
print(df['顶踩比例'].unique())


#################################################

#check if there is one defined number
# check if there is 480 and 235 in '顶踩比例'
print(df['观看次数'].isin([480,235]))

# check if there is 480 and 235 in the whole tables
print(df.isin([480,235]))


















