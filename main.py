import pandas as pd
import random
import matplotlib
matplotlib.use('TkAgg')  # Set the backend to 'TkAgg' or 'Qt5Agg'
import matplotlib.pyplot as plt

# Generate sample sales data
products = ['A', 'B', 'C', 'D', 'E']
categories = ['Category 1', 'Category 2', 'Category 3']
dates = pd.date_range(start='2022-01-01', end='2022-12-31', freq='D')

data = []
for date in dates:
    for product in products:
        category = random.choice(categories)
        sales = random.randint(100, 1000)
        data.append([product, category, date, sales])

# Create a DataFrame from the generated data
df = pd.DataFrame(data, columns=['Product', 'Category', 'Date', 'Sales'])

# Save the generated data to a CSV file
df.to_csv('sales_data.csv', index=False)

# Read the sales data from the CSV file
data = pd.read_csv('sales_data.csv')

# Display the first few rows of the data
print("Sales Data:")
print(data.head())

# Calculate total sales
total_sales = data['Sales'].sum()
print(f"\nTotal Sales: ${total_sales:.2f}")

# Calculate average sales
average_sales = data['Sales'].mean()
print(f"Average Sales: ${average_sales:.2f}")

# Find the product with the highest sales
top_product = data.loc[data['Sales'].idxmax()]
print(f"\nTop Product:")
print(f"Product: {top_product['Product']}")
print(f"Category: {top_product['Category']}")
print(f"Sales: ${top_product['Sales']:.2f}")

# Group sales by category and calculate total sales for each category
sales_by_category = data.groupby('Category')['Sales'].sum()
print(f"\nSales by Category:")
print(sales_by_category)

# Visualize sales by category using a bar chart
plt.figure(figsize=(10, 6))
sales_by_category.plot(kind='bar')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.title('Sales by Category')
plt.show()

# Analyze sales trend over time
sales_trend = data.groupby(pd.Grouper(key='Date', freq='M'))['Sales'].sum()
print(f"\nSales Trend:")
print(sales_trend)

# Visualize sales trend using a line chart
plt.figure(figsize=(10, 6))
sales_trend.plot(kind='line')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Trend')
plt.show()
