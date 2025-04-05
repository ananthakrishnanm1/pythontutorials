import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales.csv')

plt.scatter(df['month_number'], df['toothpaste'])
plt.title('Toothpaste Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()

df[['facecream', 'facewash']].plot(kind='bar')
plt.title('Face Cream and Face Wash Sales')
plt.show()

total_sales = df[['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']].sum()
total_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title('Total Sales for Each Product')
plt.show()
