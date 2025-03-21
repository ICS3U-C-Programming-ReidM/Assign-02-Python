#!/usr/bin/env python3

# Created By: Reid MacLean
# Date: March 21, 2025
# This program calculates the volume and surface area of a nonagonal prism with user input

import math


def nonagonal_prism_calculator():
    # Display welcome message
    print("Hello! Welcome to the Nonagonal Prism Calculator.")
    print("I can help you calculate the volume and surface area of a nonagonal prism.")

    # Prompt user for inputs
    a = float(input("Please enter the base edge length (a): "))
    h = float(input("Please enter the height of the prism (h): "))

    # Calculate the surface area of the nonagonal prism
    surface_area = 9 * a * h + (9 / 2) * a**2 * (1 / math.tan(math.radians(180 / 9)))

    # Calculate the volume of the nonagonal prism
    volume = (9 / 4) * a**2 * (1 / math.tan(math.radians(180 / 9))) * h

    # Display the results
    print(f"The surface area of the nonagonal prism is: {surface_area:.2f}")
    print(f"The volume of the nonagonal prism is: {volume:.2f}")


# Call the function to run the calculator
nonagonal_prism_calculator()
