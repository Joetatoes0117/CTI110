# Joseph Penner
# 10/04/2024
# P2LAB1
# This program calculates the diameter, circumference, and area of a circle based on a given radius.

import math

def main():
    # Prompt the user for the radius of the circle
    radius = float(input("Enter the radius of the circle: "))
    
    # Calculate the diameter
    diameter = radius * 2
    
    # Calculate the circumference
    circumference = 2 * math.pi * radius
    
    # Calculate the area
    area = math.pi * (radius ** 2)
    
    # Display the results
    print("\n----- Circle Calculations -----")
    print(f"Diameter: {diameter:.1f}")
    print(f"Circumference: {circumference:.2f}")
    print(f"Area: {area:.3f}")

if __name__ == "__main__":
    main()
