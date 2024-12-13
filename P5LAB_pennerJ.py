# Joseph Penner
# 11/15/2024
# P5LAB: Self-Checkout Change Dispenser
# This program simulates a self-checkout machine that calculates and dispenses change using dollars and coins.

import random

def disperse_change(change_owed):
    """
    This function calculates and displays the amount of dollars and coins needed
    to give back the change owed to the customer.
    :param change_owed: float, the amount of change to return
    """
    # Denominations in cents
    dollar = 100
    quarter = 25
    dime = 10
    nickel = 5
    penny = 1
    
    # Convert change_owed to cents
    change_in_cents = int(round(change_owed * 100))
    
    # Calculate the number of each denomination
    num_dollars = change_in_cents // dollar
    change_in_cents %= dollar
    
    num_quarters = change_in_cents // quarter
    change_in_cents %= quarter
    
    num_dimes = change_in_cents // dime
    change_in_cents %= dime
    
    num_nickels = change_in_cents // nickel
    change_in_cents %= nickel
    
    num_pennies = change_in_cents // penny
    
    # Display the results
    print(f"Change owed: ${change_owed:.2f}")
    print(f"Dollars: {num_dollars}")
    print(f"Quarters: {num_quarters}")
    print(f"Dimes: {num_dimes}")
    print(f"Nickels: {num_nickels}")
    print(f"Pennies: {num_pennies}")

def main():
    """
    Main function to simulate the self-checkout process.
    """
    # Generate a random total owed
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"The total owed is: ${total_owed:.2f}")
    
    # Prompt the user for cash input
    while True:
        try:
            cash_given = float(input("Enter the amount of cash you will pay: $"))
            if cash_given < total_owed:
                print("Insufficient amount. Please enter an amount greater than or equal to the total owed.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    # Calculate change
    change_owed = cash_given - total_owed
    
    # Call the disperse_change function
    disperse_change(change_owed)

# Call the main function
if __name__ == "__main__":
    main()
