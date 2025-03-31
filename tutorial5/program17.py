import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('weather.csv')

print("First 10 rows of weather data:")
print(df.head(10))

max_temp = df['temperature'].max()
min_temp = df['temperature'].min()

print(f"\nMaximum temperature: {max_temp}")
print(f"Minimum temperature: {min_temp}")

places_below_28 = df[df['temperature'] < 28]['place']
print("\nPlaces with temperature less than 28°C:")
print(places_below_28)

places_cloudy = df[df['weather'] == 'Cloudy']['place']
print("\nPlaces with weather 'Cloudy':")
print(places_cloudy)

weather_frequency = df['weather'].value_counts().sort_index()
print("\nWeather and its frequency:")
print(weather_frequency)

plt.figure(figsize=(10, 6))
plt.bar(df['date'], df['temperature'], color='skyblue')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Temperature of Each Day')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
