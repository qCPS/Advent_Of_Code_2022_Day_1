calories_file = open("calories.txt", "r")

calories_list = []

new_calories_list = []

calories_lines = calories_file.readlines()

calories_totals = []

top_3_calories = []

pass

for line in calories_lines:
    if line != "\n":
        line.replace("\n", "")
        new_calories_list.append(int(line))

    else:
        calories_list.append(new_calories_list)
        new_calories_list = []

pass

for i in range(len(calories_list)):
    calories_totals.append(sum(calories_list[i]))

pass

for i in range(3):
    max_calories = max(calories_totals)
    top_3_calories.append(max_calories)
    calories_totals.remove(max_calories)

print(max(top_3_calories))
print(sum(top_3_calories))
