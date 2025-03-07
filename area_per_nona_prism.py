#!/usr/bin/env python3

# Created by: Reid MacLean
# Created on: March 6, 2025
# This program calculates and displays the surface area and volume of a nonagonal prism with user input

import math


# Function to calculate the cotangent of an angle
def cotangent(angle_in_degrees):
    return 1 / math.tan(math.radians(angle_in_degrees))


# Main function to calculate surface area and volume of the nonagonal prism
def nonagonal_prism_calculator():
    # Display greeting message
    print("Hello! Welcome to the Nonagonal Prism Calculator.")
    print("I can help you calculate the volume and surface area of a nonagonal prism.")

    # Prompt user for the necessary inputs
    base_edge_a = float(input("Please enter the base edge length (base_edge_a) (cm): "))
    height_h = float(input("Please enter the height of the prism (height_h) (cm): "))

    # Calculate the surface area of the nonagonal prism
    surface_area = 9 * base_edge_a * height_h + (9 / 2) * base_edge_a**2 * cotangent(
        180 / 9
    )

    # Calculate the volume of the nonagonal prism
    volume = (9 / 4) * base_edge_a**2 * cotangent(180 / 9) * height_h

    # Display the calculated results
    print(f"The surface area of the nonagonal prism is (cm^2): {surface_area:.2f} ")
    print(f"The volume of the nonagonal prism is (cm^3): {volume:.2f} ")


# Run the program
nonagonal_prism_calculator()
