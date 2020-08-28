import pandas as pd

filePath = r"C:/Users/htian/Desktop/book in reading/python littlefly learning/Lesson15/Lesson15.xlsx"
df1 = pd.read_excel(filePath,sheet_name = "Sheet1")
df2 = pd.read_excel(filePath,sheet_name = "Sheet2")
print("df1:")
print(df1)
print("df2:")
print(df2)

df3 = pd.concat([df1,df2],ignore_index=True)
print(df3)

#### export to excel#########
resultPath = r"C:/Users/htian/Desktop/book in reading/python littlefly learning/Lesson15/results.xlsx"
df3.to_excel(resultPath, sheet_name = "together",index=False, na_rap = 0, inf_rep=0)


# 导入到多张Sheet
writer = pd.ExcelWriter(resultPath,engine = "xlsxwriter")

df3.to_excel(writer,sheet_name = "班级汇总有索引")

df3.to_excel(writer,sheet_name = "班级汇总无索引",index = False)
# 导出部分列
df3.to_excel(writer,sheet_name = "只导出姓名列和成绩列",index = False,columns = ["姓名","成绩"])

writer.save()
