import os
import math
import csv
#os.chdir('dougstuff')
print()

life_expectancies = []  # Initialize an empty list to store life expectancies

with open("life-expectancy.csv") as data_set:
    next(data_set)
    for row in data_set:
        row = row.split(",")

        entity = row[0].strip()
        code = row[1].strip()
        year = int(row[2])
        life_expectancy = float(row[3])  # Convert to float

        life_expectancies.append(life_expectancy)  # Add life expectancy to the list

# Calculate statistics after processing all data
max_life = max(life_expectancies)
min_life = min(life_expectancies)
avg_life = sum(life_expectancies) / len(life_expectancies)



max_life = -1
min_life = min(life_expectancy)
avg_life = sum(life_expectancy) / len(life_expectancy)

max_country = ""
max_year = int(max(year))
min_year = int(min(year))
min_country = min(entity)

chosen_year = ""

print()
year_lookup = input(float("Enter the year of interest: "))
print()

if chosen_year == year_lookup:
    chosen_year = year_lookup
    print(f"For the year: {year_lookup}.\n")
    print(f"The average life expectancy across all countries was str{avg_life:.2f}\n")
    print(f"The max life expectancy was in {max_country} with {max_life:.2f}\n")
    print(f"The min life expectancy was in {min_country} with {min_life:.2f}\n")

    if life_expectancy > max_life:

        max_life = life_expectancy
        max_country = entity

    print()
    print(f"The overall max life expectancy is:{max_life:.2f} from {max_country} in {max_year:.2f}.\n")
    print(f"The overall min life expectancy is:{min_life:.2f} from {min_country} in {min_year:.2f}.\n")