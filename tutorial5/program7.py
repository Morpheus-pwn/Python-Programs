import pandas as pd
import numpy as np

def analyze_auto_data(file_path):

    try:
        df = pd.read_csv(file_path)
        df = df.replace('?', np.nan) 
        df['average-mileage'] = pd.to_numeric(df['average-mileage'], errors='coerce') #convert to numeric
        df['price'] = pd.to_numeric(df['price'], errors='coerce') # convert to numeric
        df = df.fillna(method='ffill') # forward fill missing values

        df = df.drop_duplicates()

        df.to_csv('cleaned_auto.csv', index=False)

        most_expensive_company = df.loc[df['price'].idxmax()]['company']
        print(f"Most expensive car company: {most_expensive_company}")

        toyota_cars = df[df['company'] == 'toyota']
        print("\nToyota car details:\n", toyota_cars)

        total_cars_by_company = df['company'].value_counts()
        print("\nTotal cars by company:\n", total_cars_by_company)

        highest_priced_car = df.loc[df['price'].idxmax()]
        print("\nHighest priced car:\n", highest_priced_car)

        average_mileage_by_company = df.groupby('company')['average-mileage'].mean()
        print("\nAverage mileage by company:\n", average_mileage_by_company)

        sorted_cars = df.sort_values(by='price')
        print("\nCars sorted by price:\n", sorted_cars)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = 'auto.csv' 
analyze_auto_data(file_path)