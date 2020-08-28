import pandas as pd
from datetime import datetime
from dateutil.parser import parse
from pandas.tseries.offsets import Day,Hour,Minute

df1= pd.read_excel(r"Lesson14/Lesson14.xlsx")
df2= pd.read_excel(r"Lesson14/Lesson14.xlsx",sheet_name='Sheet2')
print(df1,'\n')
print(df2,'n')

################direct merge together#########

print(pd.merge(df1,df2))


############### merge with repeated data###############
df3= pd.read_excel(r"Lesson14/Lesson14.xlsx", sheet_name='Sheet3')
print(df3)
print(pd.merge(df1,df3))

##############merge multiple repeated data@#############
df4= pd.read_excel(r"C:/Users/htian/Desktop/book in reading/python littlefly learning/Lesson14/Lesson14.xlsx", sheet_name='Sheet4')
print(df4)

print(pd.merge(df1,df4))

filePath = r"C:/Users/htian/Desktop/book in reading/python littlefly learning/Lesson14/Lesson14.xlsx"
print(filePath)
df5 = pd.read_excel(filePath,sheet_name="Sheet5")
print(df5)

################ identify common colmns##############
print(pd.merge(df1,df5,on = ["姓名","学号"]))

#################use index as key###########
print(pd.merge(df1,df5,left_index=True,right_index=True))



###########may not have same number extreme condition#######
df1 = pd.read_excel(filePath,sheet_name="Sheet1")
df7 = pd.read_excel(filePath,sheet_name="Sheet7")
print(df7)

## df1 and df 7 are very different######

##########interesection########
print(pd.merge(df1,df7,how = "inner"))
print(pd.merge(df1,df7,how = "left"))
print(pd.merge(df1,df7,how = "right"))

###############union##########
print(pd.merge(df1,df7,how = "outer"))

#####################################################################
################combine layer by layer###############

df8 = pd.read_excel(filePath,sheet_name="Sheet8")
print(df8)

df9= pd.read_excel(r"C:/Users/htian/Desktop/book in reading/python littlefly learning/Lesson14/Lesson14.xlsx", sheet_name='Sheet9')
print(df9)

##############simple concrete##################
print(pd.concat([df8,df9]))
print(pd.concat([df8,df9],ignore_index=True))


df10= pd.read_excel(r"C:/Users/htian/Desktop/book in reading/python littlefly learning/Lesson14/Lesson14.xlsx", sheet_name='Sheet10')
print(df10)

print(pd.concat([df9,df10],ignore_index=True))

################## concret drop repeating data########
print(pd.concat([df9,df10],ignore_index=True).drop_duplicates())



















