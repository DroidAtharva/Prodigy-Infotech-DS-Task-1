# Prodigy-Infotech-DS-Task-1
# 🌍 Population Visualization (2024)

This project visualizes the population of the first five countries from a World Bank dataset using a bar chart.

## 📌 Description
The code reads population data from a `.csv` file (`API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv`), selects the top 5 countries, and plots their 2024 population using matplotlib.

## 📊 Technologies Used
- Python
- Pandas
- Matplotlib

## 📁 Dataset
- File: API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv
- Source: World Bank Open Data (Total Population Indicator)

## 🚀 How to Run
1. Install requirements:
   pip install pandas matplotlib

2. Place the dataset in the same directory.

3. Run the Python file:
   python population_visualization.py

## 📈 Output
A bar chart showing:
- Country Name (X-axis)
- Population in 2024 (Y-axis)

## 🧠 Learnings
- Reading and manipulating CSV with pandas
- Creating bar plots with matplotlib
- Using skiprows to remove metadata from raw datasets
