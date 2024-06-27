import numpy as num
import matplotlib.pyplot as plt
w=0.4
x=["CSE", "IT","CE", "ETC", "EEE"]
boys=[125,61,63,57,44]
girls=[28,15,9,10,5]
plt.bar(x,boys,w, label=boys)
plt.bar(x,girls,w,bottom=boys, label=girls)
plt.xlabel("Courses")  
plt.ylabel("Students")
plt.title("Students vs Courses")
plt.legend(["boys","girls"])
plt.show()
