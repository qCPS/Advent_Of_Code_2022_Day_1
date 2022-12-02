# Open the input file
calories_file = open("calories.txt", "r")

# Initialise the list for the calories each elf has
calories_list = []

# Initialise the list for the calories to add to previous list
new_calories_list = []

# Make a list with the lines from the input file
calories_lines = calories_file.readlines()

# Initialise the list of totals
calories_totals = []

# Initialise the list of top 3 highest calorie totals
top_3_calories = []

# Iterate over the lines from the input file
for line in calories_lines:

    # Check if the line contains a calorie count
    if line != "\n":

        # Remove the new line escape character
        line.replace("\n", "")

        # Add the calorie count to new_calories_list
        new_calories_list.append(int(line))

    else:

        # Add the calorie counts to the list of calories per elf
        calories_list.append(new_calories_list)

        # Reset new_calories_list
        new_calories_list = []

# Iterate over the list of calories per elf
for i in range(len(calories_list)):

    # Add the sum of each elf's calories to the totals
    calories_totals.append(sum(calories_list[i]))

# Print solution to part 1
print(max(calories_totals))

for i in range(3):

    # Initialise a variable to store the max calories
    max_calories = max(calories_totals)

    # Add max calories to top 3
    top_3_calories.append(max_calories)

    # Remove the max calories from the totals list
    calories_totals.remove(max_calories)

# Print solution to part 2
print(sum(top_3_calories))
