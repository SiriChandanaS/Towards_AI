import matplotlib.pyplot as plt
x=['C','C++','Java','Python']
y=[1,2,3,3]
c=["r","y","g","b"]
#plt.plot(x,y)
plt.title("Programming Languages",fontsize=20)
plt.xlabel("Languages",fontsize=20)
plt.ylabel("Year",fontsize=20)
plt.bar(x,y,color=c,edgecolor="black",linewidth=4)
plt.show()
