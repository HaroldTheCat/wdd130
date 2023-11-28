import os
import math
import csv

os.chdir('DATA')
print()

life_expectancies = []  # Initialize an empty list to store life expectancies
years = []  # Initialize an empty list to store years

with open("life-expectancy.csv") as data_set:
    next(data_set)
    for row in data_set:
        row = row.split(",")

        entity = row[0].strip()
        code = row[1].strip()
        year = int(row[2])
        life_expectancy = float(row[3])  # Convert to float

        life_expectancies.append(life_expectancy)  # Add life expectancy to the list
        years.append(year)  # Add year to the list

# Calculate statistics after processing all data
max_life = max(life_expectancies)
min_life = min(life_expectancies)
avg_life = sum(life_expectancies) / len(life_expectancies)

max_life_country = ""
min_life_country = ""

# Iterate over the data to find the corresponding country for max and min life expectancy
for entity, life in zip(life_expectancies, life_expectancies):
    if life == max_life:
        max_life_country = entity
    elif life == min_life:
        min_life_country = entity

max_year = max(years)
min_year = min(years)

print()
year_lookup = int(input("Enter the year of interest: "))
print()

# Update chosen_year here
chosen_year = year_lookup

if chosen_year == year_lookup:
    print(f"For the year: {year_lookup}.\n")
    print(f"The average life expectancy across all countries was {avg_life:.2f}\n")
    print(f"The max life expectancy was in {max_life_country} with {max_life:.2f}\n")
    print(f"The min life expectancy was in {min_life_country} with {min_life:.2f}\n")

print()
print(f"The overall max life expectancy is: {max_life:.2f} from {max_life_country} in {max_year}.\n")
print(f"The overall min life expectancy is: {min_life:.2f} from {min_life_country} in {min_year}.\n")

