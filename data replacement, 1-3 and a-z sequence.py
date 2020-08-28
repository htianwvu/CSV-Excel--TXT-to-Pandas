
import pandas as pd
import datetime


df = pd.read_excel(r"C:/Users/htian/Desktop/book in reading/python littlefly learning/Lesson8/Lesson8.xlsx")
df1 = df
# find the missing cell NaN
print(df,"\n")
print(df.info(),'n')

#one to one replace
df['顶踩比例'] = df['顶踩比例'].replace(2.000,1.000)
print(df,"\n")

# replace all numbers by new number
df = df.replace(2.000,1.000)
print(df,"\n")

df = df1
# replace several numbers into one new number
df = df.replace([480,34], 1314)
print(df,"\n")

df = df1
# replace several numbers into several new number
df = df.replace({480:400, 342:300})
print(df,"\n")

# 大小排序
print(df,"\n")
print(df.sort_values(by = ['观看次数'], ascending = True))
print(df.sort_values(by = ['观看次数'], ascending = False))

# /replace /change a number to non
df.loc[[1],['发布时间']] = None
print(df)

# put none in the first or last
print(df.sort_values(by = ["发布时间"], ascending = False, na_position = 'first'))
print(df.sort_values(by = ["发布时间"], ascending = False, na_position = 'last'))

# sort the sequence according two conditions
print(df.sort_values(by = ['顶踩比例', '观看次数'], ascending=[False,True]))

#数值排名
print(df['顶踩比例'])
#average of repeating numbers
print(df['顶踩比例'].rank(ascending=False,method='average'))
#first of repeating numbers
print(df['顶踩比例'].rank(ascending=False,method='first'))
#min of repeating numbers
print(df['顶踩比例'].rank(ascending=False,method='min'))
#max of repeating numbers
print(df['顶踩比例'].rank(ascending=False,method='max'))
