## pandas read excel

import pandas as pd
df = pd.read_excel(r"C:/Users/htian/Desktop/book in reading/python littlefly learning/Lesson4/Lesson4.xlsx")
print("1.excel data is", '*'*15)
print(df,"\n")

df = pd.read_excel(r"C:/Users/htian/Desktop/book in reading/python littlefly learning/Lesson4/Lesson4.xlsx",
                   sheet_name = "Sheet1")
print("1.excel data is", '*'*15)
print(df)

df = pd.read_excel(r"C:/Users/htian/Desktop/book in reading/python littlefly learning/Lesson4/Lesson4.xlsx",
                   index_col = 0)
print("2.excel data is", '*'*15)
print(df,"\n")

df = pd.read_excel(r"C:/Users/htian/Desktop/book in reading/python littlefly learning/Lesson4/Lesson4.xlsx",
                   header = 0)
print("3.excel data is", '*'*15)
print(df,"\n")

### input only a few coloums

df = pd.read_excel(r"C:/Users/htian/Desktop/book in reading/python littlefly learning/Lesson4/Lesson4.xlsx",
                   usecols = [0,3])
print("4.excel data is", '*'*15)
print(df,"\n")


# input csv

df = pd.read_csv(r"C:/Users/htian/Desktop/book in reading/python littlefly learning/Lesson4/Lesson4_csv.csv")
print("5.csv data is", '*'*15)
print(df,"\n")

df = pd.read_csv(r"C:/Users/htian/Desktop/book in reading/python littlefly learning/Lesson4/Lesson4_csv_blank.csv")
print("5.csv data is", '*'*15)
print(df,"\n")

df = pd.read_csv(r"C:/Users/htian/Desktop/book in reading/python littlefly learning/Lesson4/Lesson4_csv_blank.csv", sep = ' ')
print("6.csv data is", '*'*15)
print(df,"\n")

df = pd.read_csv(r"C:/Users/htian/Desktop/book in reading/python littlefly learning/Lesson4/Lesson4_csv_blank.csv", 
                 sep = ' ', nrows = 3)
print("7.csv data is", '*'*15)
print(df,"\n")


## input txt

df = pd.read_table(r"C:/Users/htian/Desktop/book in reading/python littlefly learning/Lesson4/Lesson4_csv_blank.txt", 
                   sep = ' ')
print("7.txt data is", '*'*15)
print(df,"\n")


## firstly familir the data
print(df.head(3),"\n")

print(df.shape,"\n")

print(df.info(),"\n")


print("distribution")
print(df.describe())


