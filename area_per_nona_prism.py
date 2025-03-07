#!/usr/bin/env python3

# Created by: Reid MacLean
# Created on: March 6, 2025
# This program calculates and displays the surface area and volume of a nonagonal prism with user input

import math


# Function to calculate the cotangent of an angle
def cotangent(angle_in_degrees):
    return 1 / math.tan(math.radians(angle_in_degrees))


# Function to convert units (cm to meters or vice versa)
def convert_units(value, unit_from, unit_to):
    conversion_factors = {
        ("cm", "m"): 0.01,
        ("m", "cm"): 100,
    }
    return value * conversion_factors.get((unit_from, unit_to), 1)


# Main function to calculate surface area and volume of the nonagonal prism
def nonagonal_prism_calculator():
    # Display greeting message
    print("Hello! Welcome to the Nonagonal Prism Calculator.")
    print("I can help you calculate the volume and surface area of a nonagonal prism.")
   
    # Allow user to choose units
    unit_choice = input("Which units would you like to use for input and output? (cm/m): ").lower()
    while unit_choice not in ["cm", "m"]:
        unit_choice = input("Invalid choice. Please choose 'cm' or 'm': ").lower()

    # Prompt user for the necessary inputs
    base_edge_a = float(input("Please enter the base edge length (base_edge_a): "))
    while base_edge_a <= 0:
        print("Edge length must be a positive value!")
        base_edge_a = float(input("Please enter the base edge length (base_edge_a): "))

    height_h = float(input("Please enter the height of the prism (height_h): "))
    while height_h <= 0:
        print("Height must be a positive value!")
        height_h = float(input("Please enter the height of the prism (height_h): "))

    # Calculate the surface area of the nonagonal prism
    surface_area = 9 * base_edge_a * height_h + (9 / 2) * base_edge_a**2 * cotangent(180 / 9)

    # Calculate the volume of the nonagonal prism
    volume = (9 / 4) * base_edge_a**2 * cotangent(180 / 9) * height_h

    # Convert units if necessary
    if unit_choice == "m":
        surface_area = convert_units(surface_area, "cm", "m")  # Convert surface area
        volume = convert_units(volume, "cm", "m")  # Convert volume

    # Display the calculated results
    print(f"\nThe surface area of the nonagonal prism is ({unit_choice}^2): {surface_area:.2f}")
    print(f"The volume of the nonagonal prism is ({unit_choice}^3): {volume:.2f}")

    # Store previous results
    previous_results = {
        "base_edge_a": base_edge_a,
        "height_h": height_h,
        "surface_area": surface_area,
        "volume": volume
    }

    # Ask the user if they want to perform another calculation
    another_calculation = input("\nWould you like to perform another calculation? (yes/no): ").lower()
    if another_calculation == "yes":
        nonagonal_prism_calculator()
    else:
        print("Thank you for using the Nonagonal Prism Calculator!")


# Run the program
nonagonal_prism_calculator()
