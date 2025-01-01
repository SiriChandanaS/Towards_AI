import pandas as pd
dataFrame=pd.read_csv(r"C:\Users\HP 735 G6\OneDrive\Desktop\projects\basic_py_programs\Book1.csv")
print(dataFrame)
print(dataFrame.head(2))#prints the number of rows as declared (Default value is 5)
print(dataFrame.tail(2))#prints the number of rows as declared (not [::-1])(Default value is 5)
print(dataFrame.info)#should be one of the very first commands you run after loading your data
print(dataFrame.shape)#info about number of rows, columns
df=dataFrame._append(dataFrame)
print(df.shape)##Using append() will return a copy without affecting the original DataFrame. We are capturing this copy in temp so we aren't working with the real data.
df=dataFrame.drop_duplicates()
print(df.shape)#deop duplicates
print(dataFrame['apples'].describe)
print(dataFrame.describe)
print(pd.__version__)
