import pandas as pd

df = pd.read_csv('employee.csv')

print(df.head(7))
print(df['name'].sort_values())
highest_salary_employee = df.loc[df['salary'].idxmax()]['name']
male_employees = df[df['gender'] == 'Male']
print(df['team'].unique())
