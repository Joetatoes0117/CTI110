# Joseph Penner
# 11/9/24
# Assignment: P4HW1
# Description: Program to collect a set of scores, calculate average after dropping the lowest score,
# and display a letter grade based on the average.

# Ask user for the number of scores to enter
num_scores = int(input("Enter the number of scores you would like to enter: "))
scores = []  # List to hold valid scores

# Loop to collect the scores
for i in range(num_scores):
    while True:
        try:
            score = float(input(f"Enter score #{i+1}: "))
            if 0 <= score <= 100:
                scores.append(score)
                break  # Exit loop if the score is valid
            else:
                print("Invalid score! Score should be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

# Find the lowest score and display it
lowest_score = min(scores)
print("\nLowest score entered:", lowest_score)

# Remove the lowest score and display the modified list
scores.remove(lowest_score)
print("Modified score list:", scores)

# Calculate the average of modified scores
average_score = sum(scores) / len(scores)
print("Average score after dropping the lowest:", format(average_score, ".2f"))

# Determine the letter grade
if average_score >= 90:
    letter_grade = 'A'
elif average_score >= 80:
    letter_grade = 'B'
elif average_score >= 70:
    letter_grade = 'C'
elif average_score >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Display the letter grade
print("Letter grade for the average score:", letter_grade)
