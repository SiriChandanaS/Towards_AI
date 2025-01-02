"""import matplotlib.pyplot as plt
x= [1, 4, 5, 3]
y= [3, 5, 7, 2]
plt.scatter(x,y)
plt.show() """
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('bmh')
df=pd.read_csv(r"C:\Users\HP 735 G6\OneDrive\Desktop\projects\basic_py_programs\Book1.csv")
#x = df['apples']
#y = df['oranges']
plt.xlabel('apples', fontsize=18)
plt.ylabel('oranges', fontsize=16)
#plt.scatter(x,y)
plt.pie(df['apples'])
plt.show()
