import pandas as pd
import matplotlib.pyplot as plt

# Read the sales data from a CSV file
data = pd.read_csv('sales_data.csv')

# Convert the date column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Analyze sales trends over time
monthly_sales = data.groupby(data['Date'].dt.to_period('M')).sum()

# Create a line chart to visualize sales trends
monthly_sales.plot(kind='line', y='Sales', figsize=(10, 6))
plt.title('Sales Trends')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()

# Identify peak sales hours
data['Hour'] = pd.to_datetime(data['Time']).dt.hour
hourly_sales = data.groupby('Hour').sum()

# Create a bar chart to visualize peak sales hours
hourly_sales.plot(kind='bar', y='Sales', figsize=(10, 6))
plt.title('Peak Sales Hours')
plt.xlabel('Hour')
plt.ylabel('Sales')
plt.show()

# Identify popular products
popular_products = data['Product'].value_counts().head(5)

# Create a pie chart to visualize popular products
popular_products.plot(kind='pie', figsize=(10, 6))
plt.title('Popular Products')
plt.ylabel('')
plt.show()

# Generate a report for store management
report = '''
Sales Trends:
{}
Peak Sales Hours:
{}
Popular Products:
{}
'''.format(monthly_sales, hourly_sales, popular_products)

print(report)



