
import pandas as pd
import datetime


df = pd.read_excel(r"C:/Users/htian/Desktop/book in reading/python littlefly learning/Lesson7/Lesson7.xlsx")
df1 = df
# find the missing cell NaN
print(df,"\n")
print(df.info(),'n')

# check missing cell
print(df.isnull(),"n")

df.index = ['one','two','three','four','five']
print(df,"\n")

# select data from one column
print("select 名称 ")
print(df['名称'],'\n')

# select data from two columns
print("select 名称 and 观看次数 ")
print(df[['名称','观看次数']],'\n')

# select data from specific several columns
print("select several columns ")
print(df.iloc[:,[0,2]],'\n')

# select data from several continous columns
print("select several continous columns ")
print(df.iloc[:,0:3],'\n')

# select one line
print(df,"\n")
print(df.loc["one"],'\n')

# select two lines
print(df.loc[["one",'three']],'\n')

# select under conditions
print(df,"\n")
print(df[(df['观看次数'] >300) & (df['评论数'] >20)], '\n')


# select index and columns together
# loc is the name of lines and columns
# iloc is the index of lines and columns
print(df.loc[['one','three'],['名称','观看次数']],'\n')

print(df.iloc[[0,2],[0,1]],'\n')

#slice index and columns together
print(df.iloc[0:3,[0,1]],'\n')

# slice under several conditions
print(df,"\n")
print(df[df['观看次数'] > 300],[['名称','观看次数']],'\n')
