# Jay Vyas, SPC ID# 2546420, Course: COP 1000
# Collaborator: none

# Pseudocode:
# 1. Ask the user how many guitar picks they want to buy.
# 2. Check if the input is a valid positive number.
#    - If not, show an error and stop the program.
# 3. Decide the price for each pick based on how many they are buying:
#    - Less than 12: $0.25 each
#    - 12 to 23: $0.23 each
#    - 24 to 35: $0.21 each
#    - 36 or more: $0.19 each
# 4. Multiply the number of picks by the price to get the total cost.
# 5. Show the total cost in currency format with the $ sign and commas if needed.

# Prompt the user for the number of guitar picks
try:
    guitar_picks = int(input("How many guitar picks do you wish to buy? "))
    if guitar_picks <= 0:
        raise ValueError("The number of picks must be a positive integer.")
except ValueError as e:
    print(f"Invalid input: {e}")
    exit()

# Determine price per pick
if guitar_picks >= 36:
    price_per_pick = 0.19
elif guitar_picks >= 24:
    price_per_pick = 0.21
elif guitar_picks >= 12:
    price_per_pick = 0.23
else:
    price_per_pick = 0.25

# Calculate total cost
total_cost = guitar_picks * price_per_pick

# Display total cost in currency format
print(f"Total cost of guitar picks is: ${total_cost:,.2f}")
