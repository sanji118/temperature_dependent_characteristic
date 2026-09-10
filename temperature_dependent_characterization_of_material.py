import pandas as pd
import matplotlib.pyplot as plt

"CSV file"
data=pd.read_csv("C:/programming_course_1/python-course/temperature_dependent_characteristic/temperature_resistance.csv")

"Extract data"
T=data["Temperature_C"]
R=data["Resistance_Ohm"]

"Display"
print(data)

"Plot"
plt.plot(T, R, 'o-')
plt.xlabel(r"Temperature ($^\circ$C)")
plt.ylabel("Resistance ($\Omega$)")
plt.title("Temperature vs Resistance")

plt.grid(True)
plt.show()