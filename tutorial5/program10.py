import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales_data.csv')

plt.scatter(df['month_number'], df['toothpaste'])
plt.title('Toothpaste Sales Data')
plt.xlabel('Month Number')
plt.ylabel('Toothpaste Sales')
plt.show()

plt.bar(df['month_number'], df['facecream'], label='Face Cream', alpha=0.5)
plt.bar(df['month_number'], df['facewash'], label='Face Wash', alpha=0.5)
plt.title('Face Cream and Face Wash Sales Data')
plt.xlabel('Month Number')
plt.ylabel('Sales')
plt.legend()
plt.show()

total_sales = df[['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']].sum()
plt.pie(total_sales, labels=total_sales.index, autopct='%1.1f%%')
plt.title('Total Sales Data for Last Year')
plt.show()