import pandas as pd
import datetime


df = pd.read_excel(r"C:/Users/htian/Desktop/book in reading/python littlefly learning/Lesson11/Lesson11.xlsx")
df1 = df
print(df,'\n')
print(df.info(),'n')

# sum axis= 0 means colomn, axis =1 means lines
print(df['财富'].sum())
# default is column
# operation at lines
#print(df['财富'].sum(axis = 1))


print(df['财富'].mean())

print(df['财富'].max())

print(df['财富'].min())

print(df['财富'].median())

print(df['财富'].var())
print(df['财富'].std())

#obtained all basic statitiscs
print(df['财富'].describe())
