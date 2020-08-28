import pandas as pd
from datetime import datetime
from dateutil.parser import parse
from pandas.tseries.offsets import Day,Hour,Minute

df = pd.read_excel(r"C:/Users/htian/Desktop/book in reading/python littlefly learning/Lesson12/Lesson12.xlsx")
df1 = df
print(df,'\n')
print(df.info(),'n')

################
#import current time
print(datetime.now())

print('year', datetime.now().year)
print('month', datetime.now().month)
print('day', datetime.now().day)
print('weekday', datetime.now().weekday())

## full check the weekday
print('which week of the year', datetime.now().isocalendar())

##############################################
print(datetime.now().date())
print(datetime.now().time())

################################
### change the time format
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print('n')

############################################
### exchange sting with timeformat
now = datetime.now()
print(now,type(now))

### to string###########
print(str(now), type(str(now)))

##### change string to datetime##############
from dateutil.parser import parse
str_now = "2020-08-08"
time_now = parse(str_now)
print(time_now,type(time_now))
print('n')

################################################
print(df)

######################################
### select data from a special day

print("发布时间 is 2020-07-02 data")
print(df[df['发布时间'] ==datetime(2020,7,2)])


#### select data from a period###

print(df[(df['发布时间'] >datetime(2020,7,5)) & 
         (df['发布时间'] < datetime(2020,7,18))])

#####################
#########time operation

delta = datetime(2020,5,21,21,59,30) - datetime(2013,5,22,23,48,12)
print("time difference=", delta)

print("time difference in days=", delta.days)
print("time difference in seconds=", delta.seconds)

#############progress or delay one day###########
from pandas.tseries.offsets import Day,Hour,Minute
date = datetime(2008,8,8,20,0,0)

print("delay one day")
print(date + Day(1))

print("delay 10 mintes")
print(date + Minute(10))


print("before 10 mintes")
print(date - Minute(10))


















