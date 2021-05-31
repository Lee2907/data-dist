import numpy as np
import matplotlib.pyplot as plt

marks = [70,45,90,12]
names = ["Memphis","Godwin","Thando","Thabo"]

names = np.array(["Memphis","Godwin","Thando","Thabo"])
marks = np.array([70,45,90,12])
plt.bar(names,marks)
plt.show()


