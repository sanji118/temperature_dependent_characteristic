# Temperature-Dependent Resistance Analysis

## Project Overview

This project analyzes the relationship between **temperature and electrical resistance** using Python.

The program reads temperature and resistance data from a CSV file, displays the data, and creates a graph showing the relationship between temperature and resistance.

## Objectives

- Read experimental data from a CSV file
- Extract temperature and resistance values
- Display the experimental data
- Plot temperature versus resistance
- Visualize the temperature-dependent behavior of resistance

## Technologies Used

- Python
- Pandas
- Matplotlib

## Project Structure

```text

temperature_dependent_characteristic/
│
├── outputs/
│   └── temperature_vs_resistance.png
│
├── main.py
├── README.md
└── temperature_resistance.csv

Dataset

The dataset contains two main columns:

Temperature_C
Resistance_Ohm

Where:

Temperature_C = Temperature in degrees Celsius
Resistance_Ohm = Electrical resistance in ohms
Analysis

The program performs the following steps:

Loads the CSV file using Pandas.
Extracts the temperature data.
Extracts the resistance data.
Displays the dataset.
Plots temperature versus resistance.
Code

The data is loaded using Pandas:

data = pd.read_csv("temperature_resistance.csv")

T = data["Temperature_C"]
R = data["Resistance_Ohm"]

The temperature and resistance values are then plotted:

plt.plot(T, R, 'o-')

The graph uses:

X-axis: Temperature (°C)
Y-axis: Resistance (Ω)
Output
Temperature vs Resistance

![Temperature vs Resistance](outputs/Figure_1.png)

Result

The graph provides a visual representation of how the electrical resistance changes with temperature.

How to Run

Install the required libraries:

pip install pandas matplotlib

Run the program:

python main.py
Conclusion

This project demonstrates a simple Python-based method for analyzing experimental temperature-dependent resistance data.

It provides practical experience with:

Reading CSV files
Data extraction using Pandas
Data visualization
Scientific plotting using Matplotlib
Future Improvements
Calculate the temperature coefficient of resistance
Fit a trendline to the experimental data
Calculate percentage change in resistance
Compare experimental and theoretical results
Analyze different materials
Author

MST. SANJIDA AKTER