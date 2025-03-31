import pandas as pd

df = pd.read_csv('employee.csv')

print(df.head(7),"\n")

print(df['name'].sort_values())

highest_salary_employee = df.loc[df['salary'].idxmax()]['name']
print("\nEmployee with Highest Salary:", highest_salary_employee)

male_employees = df[df['gender'] == 'Male']['name']
print("\nMale Employees:\n", male_employees)

teams = df['team'].unique()
print("\nTeams Employees Belong To:\n", teams)