# Joseph Penner
# 10/27/2024
# P3HW2
# This program calculates an employee's weekly salary, including any overtime pay if the employee worked more than 40 hours.


employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked this week: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Determine overtime and regular pay
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5  # Overtime pay is 1.5 times the regular rate
    regular_hours = 40
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_hours = hours_worked

# Calculate regular pay and gross pay
regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay

# Output Section
print("\nEmployee Pay Details")
print("---------------------")
print(f"Employee Name: {employee_name}")
print(f"Pay Rate: ${pay_rate:.2f}")
print(f"Hours Worked: {hours_worked}")
print(f"Overtime Hours: {overtime_hours}")
print(f"Overtime Pay: ${overtime_pay:.2f}")
print(f"Regular Pay: ${regular_pay:.2f}")
print(f"Gross Pay: ${gross_pay:.2f}")
