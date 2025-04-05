import pandas as pd

df = pd.read_csv('auto.csv')

df.fillna(method='ffill', inplace=True)
most_expensive_car = df.loc[df['price'].idxmax()]['company']
toyota_cars = df[df['company'] == 'Toyota']
total_cars = df['company'].value_counts()
highest_price_car = df.loc[df['price'].idxmax()]
average_mileage = df['average-mileage'].mean()
sorted_by_price = df.sort_values(by='price', ascending=False)

print(most_expensive_car)
print(toyota_cars)
print(total_cars)
print(highest_price_car)
print(average_mileage)
print(sorted_by_price)
