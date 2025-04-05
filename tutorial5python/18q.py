import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('weather.csv')

print(df.head(10))
print("Max Temperature:", df['temperature'].max())
print("Min Temperature:", df['temperature'].min())
places_under_28 = df[df['temperature'] < 28]['place']
cloudy_weather = df[df['weather'] == 'Cloudy']
weather_frequency = df['weather'].value_counts()
weather_frequency.plot(kind='bar')
plt.show()

plt.bar(df['date'], df['temperature'])
plt.title('Temperature of Each Day')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.show()
