
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'Business_Analyst_Excel_Project_With_Dashboard.xlsx'
data = pd.read_excel(file_path)

# Summary statistics
print("Summary Statistics:")
print(data.describe())

# Monthly Sales Bar Chart
plt.figure(figsize=(10, 6))
plt.bar(data['Month'], data['Total Sales'], color='skyblue')
plt.title('Monthly Sales', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Monthly_Sales_Chart.png')
plt.show()

# Sales Distribution by Region
region_sales = data.groupby('Region')['Total Sales'].sum()
plt.figure(figsize=(8, 8))
plt.pie(region_sales, labels=region_sales.index, autopct='%1.1f%%', startangle=140)
plt.title('Sales Distribution by Region', fontsize=14)
plt.tight_layout()
plt.savefig('Sales_Distribution_Pie_Chart.png')
plt.show()
