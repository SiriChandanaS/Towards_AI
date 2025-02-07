import matplotlib.pyplot as plt
day=[1,2,3,4,5,6,7]
no=[2,3,4,5,7,8,1]
colors=["pink", "r", "black", "blue", "yellow","green","violet"]
sizes=[40,15,90,10,80,5,100]
plt.scatter(day,no,color=colors,s=sizes, alpha=1,marker="*",edgecolors="black",linewidth=0.2)
#can use color/c=colors for diff values, s=size ~ color , alpha is for transperancy and range (0-1)
plt.title("Scatter Plot", fontsize=15)
plt.xlabel("DAY")
plt.ylabel("NUMBER")
plt.show()
