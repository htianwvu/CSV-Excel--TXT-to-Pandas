import pandas as pd
from datetime import datetime
from dateutil.parser import parse
from pandas.tseries.offsets import Day,Hour,Minute

df = pd.read_excel(r"C:/Users/htian/Desktop/book in reading/python littlefly learning/Lesson13/Lesson13.xlsx")
df1 = df
print(df,'\n')
print(df.info(),'n')

#####################################
##### customer group#################
############ according groupby(columns) #################
print(df.groupby('客户分类'))
print(df.groupby('客户分类').count())
print(df.groupby('客户分类').sum())

## grounpby for several columns###
print(df.groupby(['客户分类','区域']).count())
print(df.groupby(['客户分类','区域']).sum())


#####
print('统计类a b v客户数量')
print(df.groupby('客户分类')['用户ID'].count())


### aggregate function###

print(df.groupby('客户分类').aggregate(['count','sum']))

## operate different in each column###
print(df.groupby('客户分类').aggregate({'用户ID':'count',"7月销量":"sum",
                                 "8月销量":'sum'}))

### dataframe####
print('values重置索引')
print(df.groupby('客户分类').sum().reset_index())


####pivot-table


# Section2 数据透视表
# pivot_table(data,values=None,index = None,columns = None,aggfunc="mean",
# fill_value = None,margins = False,dropna = True,margins_name = "All")
# data:整张表
# value：透视表的数据
# index:行索引
# columns：列索引
# aggfunc:聚合函数
# fill_value:对空值的填充值
# margins:表示是否显示合计列
# dropna:是否删除缺失，如果为true，就会删除有缺失值的行
# margins_name:合计列的列名

print(pd.pivot_table(df,values = "7月销量",index ='客户分类',
                     columns='区域',aggfunc='count'))

print(pd.pivot_table(df,values = "7月销量",index ='客户分类',
                     columns='区域',aggfunc='count',margins=True))

print(pd.pivot_table(df,values = "7月销量",index ='客户分类',
                     columns='区域',aggfunc='count', margins = True, margins_name ='total'))

#### set nan as 0###
print(pd.pivot_table(df,values = "7月销量",index ='客户分类',
                     columns='区域',aggfunc='count', margins = True, margins_name ='total',
                     fill_value = 0))
#### several costomers####
print(pd.pivot_table(df,values = ["7月销量",'8月销量','9月销量'],
                     index ='客户分类',
                     columns='区域',
                     aggfunc={"7月销量":'sum','8月销量':'sum','9月销量':'sum'}, 
                     margins = True, margins_name ='total', fill_value = 0))

#### reset index####
print(pd.pivot_table(df,values = ["7月销量",'8月销量','9月销量'],
                     index ='客户分类',
                     columns='区域',
                     aggfunc={"7月销量":'sum','8月销量':'sum','9月销量':'sum'}, 
                     margins = True, margins_name ='total', 
                     fill_value = 0).reset_index())


#### reset index

