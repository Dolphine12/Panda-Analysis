# importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Loading and Exlporing the Dataset
df = pd.read_csv('walmart_sales.csv')
print(df.head()) # Display the first few rows to inspect the data
print(df.info()) # Display the data types and non-null counts

# Basic Data Analysis
#Cleaning the Data
df.dropna(inplace=True) # Remove rows with missing values
df.drop_duplicates(inplace=True) # Remove duplicate rows

# Compute basic statistics of numerical columns
statistics = df.describe()
print(statistics)

# Grouping by 'Store' and calculating the mean of 'Weekly_Sales'
Store_Sales_mean = df.groupby('Store')['Weekly_Sales'].mean().reset_index() #Computes mean
top_5_Store = Store_Sales_mean.nlargest(5, 'Weekly_Sales') # Get top 5 stores by mean sales
top_Store = top_5_Store.sort_values(by='Weekly_Sales', ascending=False).head(1) # Sort by sales in descending order and get the top store

# Analyzing the relationship between 'Holiday_Flag' and 'Weekly_Sales'
holiday_sales = df.groupby('Holiday_Flag')['Weekly_Sales'].mean().reset_index()
print("Average Weekly Sales by Holiday Flag:")
print(holiday_sales)

# Displaying the top store
print("Top Store by Weekly Sales:")
print(top_Store)
 #Mean of Numerical Columns
mean_temp = df['Temperature'].mean()
mean_fuel_price = df['Fuel_Price'].mean()
mean_cpi = df['CPI'].mean()

print("Mean Temperature:", mean_temp)
print("Mean Fuel Price:", mean_fuel_price)
print("Mean CPI:", mean_cpi)

import pandas as pd
import matplotlib.pyplot as plt

# Group by temperature and calculate mean weekly sales
temperature_sales = df.groupby('Temperature')['Weekly_Sales'].mean().reset_index()

# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(temperature_sales['Temperature'], temperature_sales['Weekly_Sales'], color='orange', alpha=0.7)
plt.title('Temperature vs Weekly Sales')
plt.xlabel('Temperature (°F)')
plt.ylabel('Average Weekly Sales ($)')
plt.grid(True)
plt.tight_layout()
plt.show()


# Finding the day with the highest and lowest temperature
highest_temp_day = df.loc[df['Temperature'].idxmax()]
lowest_temp_day = df.loc[df['Temperature'].idxmin()]

# Calculating the difference in sales between the highest and lowest temperature days
sales_difference = highest_temp_day['Weekly_Sales'] - lowest_temp_day['Weekly_Sales']

print("Day with Highest Temperature:")
print(highest_temp_day)
print("\nDay with Lowest Temperature:")
print(lowest_temp_day)
print("\nDifference in Weekly Sales between Highest and Lowest Temperature Days:", sales_difference)



# Pie chart of top 5 stores by mean weekly sales
plt.pie(top_5_Store['Weekly_Sales'], labels=top_5_Store['Store'], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Top 5 Stores by Mean Weekly Sales')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
plt.show()

# Line chart for weekly sales trend over time
df.sort_values(by='Date', inplace=True)  # Sort the data by date

# Pick the first (earliest) date entry per store
df_unique = df.groupby('Store').first().reset_index()

# Sort again by Date for time-based plotting
df_unique.sort_values(by='Date', inplace=True)
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Weekly_Sales'], marker='o', linestyle='-', color='g', alpha=0.7)
plt.title('Weekly Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Weekly Sales ($)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Bar chart for Average Sales per Store
avg_sales_per_store = df.groupby('Store')['Weekly_Sales'].mean().reset_index()

plt.figure(figsize=(12, 6))
plt.bar(avg_sales_per_store['Store'], avg_sales_per_store['Weekly_Sales'], color='skyblue', edgecolor='black')
plt.title('Average Weekly Sales per Store')
plt.xlabel('Store')
plt.ylabel('Average Weekly Sales ($)')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Histogram of CPI
plt.hist(df['CPI'], bins=20, color='purple', edgecolor='black', alpha=0.7)
plt.title('Distribution of CPI')
plt.xlabel('CPI')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

