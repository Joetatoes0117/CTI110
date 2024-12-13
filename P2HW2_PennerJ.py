# Joseph Penner
# 11/13.2024
# P2HW2
# This program collects grades for six modules and displays statistics.

def main():
    # Create a list to store grades
    grades = []

    # Request grades for each module
    grades.append(float(input("Enter grade for Module 1: ")))
    grades.append(float(input("Enter grade for Module 2: ")))
    grades.append(float(input("Enter grade for Module 3: ")))
    grades.append(float(input("Enter grade for Module 4: ")))
    grades.append(float(input("Enter grade for Module 5: ")))
    grades.append(float(input("Enter grade for Module 6: ")))

    # Calculate statistics
    lowest_grade = min(grades)
    highest_grade = max(grades)
    total_sum = sum(grades)
    average_grade = total_sum / len(grades)

    # Display results
    print(f"\nLowest Grade: {lowest_grade:.2f}")
    print(f"Highest Grade: {highest_grade:.2f}")
    print(f"Sum of Grades: {total_sum:.2f}")
    print(f"Average Grade: {average_grade:.2f}")

if __name__ == "__main__":
    main()
