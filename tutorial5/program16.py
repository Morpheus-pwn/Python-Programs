import pandas as pd

df = pd.read_csv('student.csv')

average_cgpa = df['CGPA'].mean()
print("Average CGPA:", average_cgpa, "\n")

high_cgpa_students = df[df['CGPA'] > 9]
print("Students with CGPA > 9:\n", high_cgpa_students)

cse_high_cgpa_students = df[(df['Branch'] == 'CSE') & (df['CGPA'] > 9)]
print("\nCSE Students with CGPA > 9:\n", cse_high_cgpa_students)

max_cgpa_student = df.loc[df['CGPA'].idxmax()]
print("\nStudent with Maximum CGPA:\n", max_cgpa_student)

average_cgpa_by_branch = df.groupby('Branch')['CGPA'].mean()
print("\nAverage CGPA by Branch:\n", average_cgpa_by_branch)