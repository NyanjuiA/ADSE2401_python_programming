# Python file to demonstrate visualising student scores on a bar chart

# Import the required module
import matplotlib.pyplot as plt

names = ["Adam","Richard","William","Emy","Linda"]
scores = [86,90,79,78,96]
plt.bar(names, scores)
plt.xlabel("Student Names")
plt.ylabel("Scores")
plt.title("Test Score by Student")
plt.xticks(rotation=90)
plt.grid(axis='y')
plt.tight_layout()
# plt.plot(x_pt,y_pt,'o:r',marker='x')
plt.show()