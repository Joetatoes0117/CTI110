# Joseph Penner
# 11/24/24
# P5HW - MathQuiz
# This program provides a menu-driven math quiz with options to add or subtract random numbers. 
# The user can guess the result of the operation, and the program provides feedback.
# The program runs until the user selects the option to exit.

import random

# Function to generate two random numbers
def generate_numbers():
    return random.randint(100, 999), random.randint(100, 999)

# Function to handle addition quiz
def addition_quiz():
    num1, num2 = generate_numbers()
    correct_answer = num1 + num2
    print(f" {num1}")
    print(f"+{num2}")

    guess_count = 0
    while True:
        try:
            user_answer = int(input("Enter your answer: "))
            guess_count += 1
            if user_answer == correct_answer:
                print(f"Congratulations! You got it right in {guess_count} guesses.")
                break
            elif user_answer < correct_answer:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Please enter a valid number.")

# Function to handle subtraction quiz
def subtraction_quiz():
    num1, num2 = generate_numbers()
    correct_answer = num1 - num2
    print(f" {num1}")
    print(f"-{num2}")

    guess_count = 0
    while True:
        try:
            user_answer = int(input("Enter your answer: "))
            guess_count += 1
            if user_answer == correct_answer:
                print(f"Congratulations! You got it right in {guess_count} guesses.")
                break
            elif user_answer < correct_answer:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Please enter a valid number.")

# Function to display the menu and process user's choice
def display_menu():
    while True:
        print("\nMath Quiz")
        print("1. Add Random Numbers")
        print("2. Subtract Random Numbers")
        print("3. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                addition_quiz()
            elif choice == 2:
                subtraction_quiz()
            elif choice == 3:
                print("Thank you for playing! Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main program execution
if __name__ == "__main__":
    display_menu()
