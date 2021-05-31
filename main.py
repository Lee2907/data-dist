import numpy as np
import matplotlib.pyplot as plt

marks = [70,45,90,12]
names = ["Memphis","Godwin","Thando","Thabo"]

names = np.array(names)
marks = np.array(marks)
plt.bar(names,marks)
plt.xlabel("Names of Students")
plt.ylabel("Marks of Students")
plt.show()


