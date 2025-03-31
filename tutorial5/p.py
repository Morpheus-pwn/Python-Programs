import pandas as pd
import numpy as np
import random
from datetime import date, timedelta
import matplotlib.pyplot as plt

def generate_weather_csv(filename='weather.csv'):
    """Generates a weather.csv file with sample data."""

    start_date = date(2023, 1, 1)
    num_days = 30
    dates = [start_date + timedelta(days=i) for i in range(num_days)]
    places = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata', 'Hyderabad', 'Pune', 'Jaipur', 'Lucknow', 'Ahmedabad']
    temperatures = np.random.uniform(25, 40, size=num_days)  # Temperatures between 25 and 40°C
    weathers = np.random.choice(['Sunny', 'Cloudy', 'Rainy', 'Windy'], size=num_days)

    data = {
        'date': dates,
        'place': random.choices(places, k=num_days), #allow duplicate places
        'temperature': temperatures,
        'weather': weathers
    }

    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date']) #convert date objects to datetime64
    df.to_csv(filename, index=False)
    print(f"{filename} generated successfully.")

# Generate the weather.csv file
generate_weather_csv()