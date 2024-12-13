# Penner

# This program takes a number grade, determines the average, and displays the letter grade for the average.

# Enter grades for six modules
grades = []
for i in range(1, 7):
    grade = float(input(f'Enter grade for Module {i}: '))
    grades.append(grade)

# Determine lowest, highest, sum, and average for grades
low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

# Print the calculated values
print(f'Lowest grade: {low}')
print(f'Highest grade: {high}')
print(f'Total of grades: {total}')
print(f'Average grade: {avg:.2f}')  # Format average to two decimal places

# Determine letter grade for average
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')


