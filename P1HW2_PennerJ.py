# Joseph Penner
# 9/28/2024
# P1HW2
# This program calculates the remaining budget for a trip after expenses.

def main():
    budget = float(input('Enter your budget: $'))
    print('')
    destination = input('Enter your travel destination: ')
    print('')
    gas_expense = float(input('Enter the amount you will spend on gas: $'))
    print('')
    accommodation_expense = float(input('Enter the amount you will spend on accommodation: $'))
    print('')
    food_expense = float(input('Enter the amount you will spend on food: $'))

    total_expenses = gas_expense + accommodation_expense + food_expense

    remaining_budget = budget - total_expenses
    print('')
    print ('-----Travel Expenses-----')

    print(f'\nTravel Destination: {destination}')
    print(f'Total Expenses: ${total_expenses:.2f}')
    print(f'Remaining Budget: ${remaining_budget:.2f}')

if __name__ == "__main__":
    main()
