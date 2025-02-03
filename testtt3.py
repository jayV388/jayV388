# Pseudocode
# Define constant conversion factor
# Function to get a positive integer from the user
# Get user input for start, stop, and step values
# Print table header
# Loop through range from start to stop, with increments of step


# Constant for conversion factor (US tons to Imperial tons)
US_TO_IMPERIAL_CONVERSION = 0.892857143  # 1 US ton = 0.892857143 Imperial tons

# Function to get validated input using walrus operator
def get_positive_int(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            value = int(value)
            if value > 0:
                return value
        print("Error: Value for US tons must be a positive whole number greater than zero.")

# Getting user input for start, stop, and step values
start = get_positive_int("Enter the start for US tons: ")
stop = get_positive_int("Enter the stop for US tons: ")
step = get_positive_int("Enter the step for US tons: ")

# Ensure that stop is greater than start and step is positive and meaningful
if stop <= start:
    print("Error: Stop value must be greater than start value.")
    exit()
if step <= 0 or step > (stop - start):
    print("Error: Step value must be a positive number and not exceed the difference between start and stop.")
    exit()

# Printing table header
print(f"{'US Tons':^10} {'Imperial Tons':>13}")

# Loop to generate and display the table
for us_tons in range(start, stop + 1, step):
    imperial_tons = us_tons * US_TO_IMPERIAL_CONVERSION
    print(f"{us_tons:^10} {imperial_tons:>13.3f}")
