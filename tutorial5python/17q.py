import pandas as pd

df = pd.read_csv('student.csv')

average_cgpa = df['CGPA'].mean()
students_above_9 = df[df['CGPA'] > 9]
cse_students_above_9 = df[(df['Branch'] == 'CSE') & (df['CGPA'] > 9)]
max_cgpa_student = df.loc[df['CGPA'].idxmax()]
average_cgpa_by_branch = df.groupby('Branch')['CGPA'].mean()

print(average_cgpa)
print(students_above_9)
print(cse_students_above_9)
print(max_cgpa_student)
print(average_cgpa_by_branch)
