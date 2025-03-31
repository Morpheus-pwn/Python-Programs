import pandas as pd

data = {
    'rollno': [10001, 10002, 10003],
    'name': ['Jack', 'John', 'Alex'],
    'place': ['CityA', 'CityB', 'CityC'],
    'mark': [76, 77, 74]
}

df = pd.DataFrame(data)
df.to_csv('stud.csv', index=False)

df = pd.read_csv('stud.csv')
print(df)

df.set_index('rollno', inplace=True)

print(df[['name', 'mark']])

print(df.sort_values(by='name')[['name', 'mark']])

print(df.sort_values(by='mark', ascending=False))

average_mark = df['mark'].mean()
median_mark = df['mark'].median()
mode_mark = df['mark'].mode()[0]
print(f"Average Mark: {average_mark}, Median Mark: {median_mark}, Mode Mark: {mode_mark}")

min_mark = df['mark'].min()
max_mark = df['mark'].max()
print(f"Minimum Mark: {min_mark}, Maximum Mark: {max_mark}")

variance_mark = df['mark'].var()
std_dev_mark = df['mark'].std()
print(f"Variance: {variance_mark}, Standard Deviation: {std_dev_mark}")

import matplotlib.pyplot as plt

df['mark'].hist()
plt.title('Histogram of Marks')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.show()

df.drop(columns=['place'], inplace=True)
print(df)