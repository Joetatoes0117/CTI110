def display_multiplication_table(number):
    """Display multiplication table for a given number from 1 to 12."""
    print(f"\nMultiplication Table for {number}:")
    for i in range(1, 13):  # Use a for loop to go from 1 to 12
        print(f"{number} x {i} = {number * i}")

def main():
    while True:  # Use a while loop to allow repeated runs
        try:
            # Ask the user for an integer
            user_input = int(input("Enter a non-negative integer: "))

            if user_input < 0:
                print("Error: Cannot accept negative values.")
            else:
                display_multiplication_table(user_input)

            # Ask the user if they want to run the program again
            run_again = input("Do you want to run the program again? (yes/no): ").strip().lower()
            if run_again != "yes":
                print("Goodbye!")
                break  # Exit the loop if the user says "no"

        except ValueError:
            print("Error: Please enter a valid integer.")

# Run the main function
main()
