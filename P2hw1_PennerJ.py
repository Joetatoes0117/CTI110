# Joseph Penner
# 10/13/2024
# P2HW1
# This program calculates and displays travel expenses in a formatted table.

# Sample program to display travel expenses in a nicely formatted manner

def main():
    print("Travel Expenses Tracker")
    
    # Collect data from the user
    destinations = []
    expenses = []
    
    while True:
        destination = input("Enter a travel destination (or 'done' to finish): ")
        if destination.lower() == 'done':
            break
        
        # Input for expense and convert to float
        try:
            expense = float(input(f"Enter the expense for {destination}: $"))
        except ValueError:
            print("Please enter a valid number for the expense.")
            continue
        
        destinations.append(destination)
        expenses.append(expense)
    
    # Display results in a formatted manner
    print("\nTravel Expenses Summary")
    print(f"{'Destination':<20} {'Expense':>10}")
    print("="*30)
    
    for i in range(len(destinations)):
        print(f"{destinations[i]:<20} ${expenses[i]:>9.2f}")

if __name__ == "__main__":
    main()
