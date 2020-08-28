import pandas as pd
import datetime


df1 = pd.read_excel(r"C:/Users/htian/Desktop/book in reading/python littlefly learning/Lesson10/Lesson10.xlsx",
                    sheet_name='Sheet1')
df2 = pd.read_excel(r"C:/Users/htian/Desktop/book in reading/python littlefly learning/Lesson10/Lesson10.xlsx",
                    sheet_name='Sheet2')
print(df1,'\n')
print(df2,'\n')

########################################
#insert new line or columns
#combine two excel
df = pd.concat([df1,df2])
df.index = [0,1,2,3,4,5,6]
df3 = df.copy()
print(df)
#########################################
#insert new columns
df.insert(3,"顶的人数",[10,13,15,19,12,20,24])
print(df)

# insert column at the last
df["顶的人数"] = [10,13,15,19,12,20,24]
print(df)

#################################
#exchange line and index
print(df.T)

####################################
#apply or apply map
# add 1 to every number of column
df["观看次数"].apply(lambda x:x+1)
print(df)

### applymap add number to all columns... not useful too much



 
