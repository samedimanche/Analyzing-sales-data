# Analyzing-sales-data

A Python program that creates and fills in a CSV file with sample sales data, and then perform some basic analysis on that data.

This program generates a sample sales data file named sales_data.csv and performs analysis on it. Here's what the program does:

It generates sample sales data for a year (2022) with random products, categories, and sales amounts.
It creates a DataFrame from the generated data and saves it to a CSV file named sales_data.csv.
It reads the sales data from the CSV file using the pandas library.
It displays the first few rows of the data using data.head().
It calculates the total sales by summing the 'Sales' column.
It calculates the average sales by taking the mean of the 'Sales' column.
It finds the product with the highest sales using data.loc[data['Sales'].idxmax()].
It groups the sales data by category and calculates the total sales for each category using data.groupby('Category')['Sales'].sum().
It visualizes the sales by category using a bar chart with matplotlib.
It analyzes the sales trend over time by grouping the data by month using pd.Grouper(key='Date', freq='M').
It visualizes the sales trend using a line chart with matplotlib.
This program generates sample sales data and provides a basic analysis of the data, including total sales, average sales, top-selling product, sales by category, and sales trend over time. 
