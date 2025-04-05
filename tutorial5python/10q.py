import pandas as pd

df = pd.read_csv('stud.csv')

print(df)
df.set_index('rollno', inplace=True)
print(df[['name', 'mark']])
print(df[['rollno', 'name', 'mark']].sort_values(by='name'))
print(df[['rollno', 'name', 'mark']].sort_values(by='mark', ascending=False))
print("Average Mark:", df['mark'].mean())
print("Median Mark:", df['mark'].median())
print("Mode Mark:", df['mark'].mode()[0])
print("Min Mark:", df['mark'].min())
print("Max Mark:", df['mark'].max())
print("Variance:", df['mark'].var())
print("Standard Deviation:", df['mark'].std())
df['mark'].hist()
df.drop('place', axis=1, inplace=True)
print(df)
