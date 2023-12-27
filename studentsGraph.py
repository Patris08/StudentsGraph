import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style


classes = ["Python", "R", "AI", "ML", "Data-Science"]
class1_students = [30, 10, 20, 25, 10]
class2_students = [40, 5, 20, 20, 10]
class3_students = [35, 5, 30, 15, 15]

style.use("ggplot")
plt.figure(figsize=(13, 7)) 
plt.bar(classes, class1_students,width=0.2, align="edge", color="yellow", edgecolor="m",
        linewidth = 3, alpha=0.9, linestyle="-", label="Class1_Students", visible=True)

plt.xlabel("Classes", fontsize=13)
plt.ylabel('Students of Class1', fontsize=13)
plt.title("BarGraph for Class1 Students")
plt.show()

# JOINED 2

plt.figure(figsize=(13, 7))

classes_index = np.arange(len(classes))

width =0.2

plt.bar(classes_index, class1_students,  width,color="yellow", label="Class1_Students")
plt.bar(classes_index + width, class2_students,width,  color="green", label="Class2_Students")
plt.bar(classes_index + width + width, class3_students,width,  color="black", label="Class3_Students")
plt.xticks(classes_index + width,classes, rotation=30)
plt.xlabel("Classes", fontsize=13)
plt.ylabel('Number of Students', fontsize=13)
plt.title("BarGraph for Class 1,2 & 3 Students")
plt.show()




plt.figure(figsize=(13,7)) 

classes_index = np.arange(len(classes))

width =0.2

plt.barh(classes_index, class1_students,  width,color="yellow", label="Class1_Students")
plt.barh(classes_index + width, class2_students,width,  color="green", label="Class2_Students")
plt.barh(classes_index + width + width, class3_students,width,  color="black", label="Class3_Students")
plt.yticks(classes_index + width,classes, rotation=30)
plt.ylabel("Classes", fontsize=13)
plt.xlabel('Number of Students', fontsize=13)
plt.title("BarGraph for Class 1,2 & 3 Students")
plt.legend(loc=1)
plt.show()