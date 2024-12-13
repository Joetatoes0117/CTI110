# Joseph Penner
# 11/9/24
# Assignment: P4HW2 - Gross Pay Calculator
# Description: This program calculates the gross pay for multiple employees, 
# including overtime, regular pay, and total gross pay for all employees.


# Initialize total values for overtime, regular pay, and gross pay, as well as employee count
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

# Loop to collect and process employee data
while True:
    # Step 2a: Get employee name
    employee_name = input("Enter employee's name or 'Done' to terminate: ")

    # Step 2b: Check if the user wants to stop entering employees
    if employee_name.lower() == "done":
        break

    # Step 2c: Get hourly rate and hours worked
    try:
        pay_rate = float(input("Enter hourly pay rate: "))
        hours_worked = float(input("Enter number of hours worked: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for pay rate and hours.")
        continue

    # Step 2d: Calculate regular and overtime pay
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        regular_pay = 40 * pay_rate
    else:
        overtime_pay = 0
        regular_pay = hours_worked * pay_rate

    gross_pay = regular_pay + overtime_pay

    # Step 2e: Add to totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    # Display employee-specific information
    print(f"\nEmployee: {employee_name}")
    print(f"Regular Pay: ${regular_pay:.2f}")
    print(f"Overtime Pay: ${overtime_pay:.2f}")
    print(f"Gross Pay: ${gross_pay:.2f}\n")

# Step 3: Display totals once the user finishes entering employees
print("\n--- Summary ---")
print(f"Total Number of Employees Entered: {employee_count}")
print(f"Total Overtime Pay: ${total_overtime_pay:.2f}")
print(f"Total Regular Pay: ${total_regular_pay:.2f}")
print(f"Total Gross Pay: ${total_gross_pay:.2f}")
