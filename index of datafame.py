
import pandas as pd
import datetime


df = pd.read_excel(r"C:/Users/htian/Desktop/book in reading/python littlefly learning/Lesson6/Lesson6.xlsx")
df1 = df
# find the missing cell NaN
print(df,"\n")
print(df.info(),'n')

# check missing cell
print(df.isnull(),"n")

# dtype introduction
print(df['观看次数'].dtype,'\n')
print(df['发布时间'].dtype,'\n')


# convert dtype fo one colomn
print(df['观看次数'].astype("float64"),'\n')

# add index of lines
df.index = [1,2,3,4,5]
print(df,"\n")

# add index of specific colomn as index
df = df.set_index('观看次数')
print(df,"\n")

df = df1

# rename title/index of columns
df = df.rename(columns = {'发布时间':'新发布时间'})
print(df,"\n")











