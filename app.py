"""
Savings Goal Tracker
--------------------
This simple program asks the user how much money they plan to save per day
and estimates how many days and weeks it will take to reach a fixed savings goal.
"""

# Task 1: Initial welcome message
print("Welcome to my Python program!")
print("=== Savings Goal Tracker ===")

# Task 2: Ask the user for input
daily_savings_input = input("How many dollars do you plan to save per day? ")

# Task 5: Basic error handling for invalid input (required for Task 5)
try:
    daily_savings = float(daily_savings_input)

    if daily_savings <= 0:
        print("Please enter an amount greater than 0.")
        exit()

except ValueError:
    print("Please enter a valid number (for example, 10 or 12.50).")
    exit()

# Task 3: Perform calculation
savings_goal = 500.0
days_needed = savings_goal / daily_savings
weeks_needed = days_needed / 7

# Task 4: Display results clearly
print()
print("=== Savings Plan Summary ===")
print(f"Savings goal: ${savings_goal:.2f}")
print(f"Daily savings: ${daily_savings:.2f}")
print(f"It will take about {days_needed:.1f} days to reach your goal.")
print(f"That is roughly {weeks_needed:.1f} weeks.")

# Task 6: Final cleanup and comments (required for Task 6)
# The program now includes:
# - Welcome message
# - User input section
# - Error handling to protect from invalid input
# - Calculations for days and weeks needed
# - Clear, formatted output for the user
