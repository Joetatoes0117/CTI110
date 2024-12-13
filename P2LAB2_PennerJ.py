# Joseph Penner
# 10/05/2024
# P2LAB2
# This program calculates the gallons of gas needed for a given vehicle based on user input.

def main():
    # Create a dictionary with vehicle MPG values
    vehicle_mpg = {
        "Camaro": 18.21,
        "Prius": 52.36,
        "Model S": 110,
        "Silverado": 26
    }

    # Get all keys from the dictionary
    keys = vehicle_mpg.keys()
    
    # Print the keys
    print("Available vehicles:")
    print(", ".join(keys))

    # Prompt user for a vehicle
    vehicle = input("Enter a vehicle from the list: ")

    # Check if the vehicle is in the dictionary
    if vehicle in vehicle_mpg:
        # Display the MPG for the selected vehicle
        mpg = vehicle_mpg[vehicle]
        print(f"{vehicle} MPG: {mpg}")

        # Prompt user for miles to drive
        miles = float(input("Enter the number of miles you will drive: "))

        # Calculate gallons of gas needed
        gallons_needed = miles / mpg

        # Display the result rounded to two decimal places
        print(f"Gallons of gas needed: {gallons_needed:.2f}")
    else:
        print("Vehicle not found in the list.")

if __name__ == "__main__":
    main()
