# Sales Data Analysis Project
## Analyzing Data with Pandas and Visualizing Results with Matplotlib

## 📊 Overview

This project involves the exploration and analysis of a sales dataset using Python and the Pandas library. The aim was to uncover patterns and relationships between various variables, particularly focusing on how **holiday flags** and **temperature** influence **sales performance**.

---

## 🧾 Dataset

- Format: CSV
- Content: The dataset includes weekly sales data from Walmart_Store along with related factors such as fuel price, temperature, holiday indicators, and CPI (Consumer Price Index).

---

## 🧹 Data Cleaning

- I Loaded the dataset using `pandas.read_csv()`
- Then Inspected the data with `.head()` and `.info()`
- I Checked for missing values using `.isnull().sum()`
- Handled missing data by:
  - Dropping rows with critical missing values
  - Filling in minor missing values with appropriate strategies (e.g., using `.fillna()` with mean or forward fill)

---

## 🎯 Analysis Objective

The main objectives of this analysis were:
- To Find the Store with the most average **Weekly Sales**.
- To examine the relationship between **holiday flags** and **weekly sales**
- To assess whether **temperature changes** impacted sales trends
- To identify any other interesting patterns across stores and economic indicators (CPI, Fuel Price, etc.)

---

## 📈 Task Summary

### Task 1: Load and Explore the Dataset
- Loaded the dataset using `pandas`
- Displayed the first few rows with `.head()`
- Explored data types, missing values, and structure
- Cleaned and preprocessed data

### Task 2: Basic Data Analysis
- Computed basic statistics: `.describe()` (mean, median, standard deviation)
- Performed groupings:
  - Grouped data by **Store** and **Holiday_Flag**, and calculated average sales
- Identified:
  - Stores with the highest and lowest average sales
  - Sales dips or peaks around holidays and extreme temperatures

### Task 3: Data Visualization

Created the following visualizations using `matplotlib` and `seaborn`:
1. **Line Chart**: Weekly sales trends over time
2. **Bar Chart**: Average sales per store
3. **Histogram**: Distribution of sales
4. **Scatter Plot**: Relationship between temperature and weekly sales
5. **Bar Chart**: Top 5 weekly_Sales.

Each chart includes appropriate:
- Titles
- X and Y axis labels
- Legends (where applicable)

---

## 📌 Key Findings

- Sales tend to **drop during extreme temperatures**, indicating weather impacts consumer behavior.
- Certain stores consistently outperform others, even during holidays.
- **Holiday_Flag** has mixed effects: some holidays boost sales, while others see declines.

---

## 📁 Files Included

- `Sales.py`: Python File
- `Walmart_Sales.csv`: Cleaned dataset
- `README.md`: This file

---

## 🧠 Future Work

- Incorporate promotional or marketing data to understand external factors better
- Expand the dataset to include more years or geographic regions
- Use machine learning models to predict future sales trends

