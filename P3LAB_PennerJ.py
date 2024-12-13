# Joseph Penner
# P3LAB
# This program calculates the most efficient number of dollars, quarters,
# dimes, nickels, and pennies needed to make a given amount of money.

def main():
    # Prompt user for input
    money_input = float(input("Enter an amount of money:"))
    
    # Convert money to cents to avoid floating point issues
    total_cents = int(money_input * 100)

    # Calculate the number of each denomination
    dollars = total_cents // 100
    total_cents %= 100
    
    quarters = total_cents // 25
    total_cents %= 25
    
    dimes = total_cents // 10
    total_cents %= 10
    
    nickels = total_cents // 5
    pennies = total_cents % 5

    # Display results
    if dollars > 0:
        print(f"{dollars} dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        print(f"{quarters} quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} penn{'ies' if pennies > 1 else 'y'}")

# Call the main function
if __name__ == "__main__":
    main()
