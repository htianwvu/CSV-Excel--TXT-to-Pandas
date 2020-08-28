# deal with empty cell

import pandas as pd
import datetime


df = pd.read_excel(r"C:/Users/htian/Desktop/book in reading/python littlefly learning/Lesson5/Lesson5.xlsx")


# find the missing cell NaN
print(df,"\n")
print(df.info(),'n')

# check missing cell

print(df.isnull(),"n")

# delelte the lines containing missing cell
df1 = df
print(df.dropna())


# delete the lines which containing all nan
print(df.dropna(how = "all"))

# fill the nan as 0
print(df.fillna(0),'\n')

# fill the nan as specific format such as time
df=df1
datetime_p = datetime.datetime.strptime("2020/7/20 00:00:00",r'%Y/%m/%d %H:%M:%S')
print(df.fillna({"顶踩比例":0,"发布时间":datetime_p}))

# deal with repeating data
df = pd.read_excel(r"C:/Users/htian/Desktop/book in reading/python littlefly learning/Lesson5/Lesson5.xlsx",
                   sheet_name="Sheet2")
df1 = df
print(df1)

# delete duplicate, keep the last line

print(df.drop_duplicates(subset="名称", keep="last"),"\n")

# delete duplicate, keep the first line
print(df.drop_duplicates(subset="名称", keep="first"),"\n")

#delete duplucate with same two columns
print(df.drop_duplicates(subset=["名称","观看次数"]), "\n")



