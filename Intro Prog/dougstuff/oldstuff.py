import os
import math
import csv
#os.chdir('dougstuff')
print()

life_expectancy_values = []
years = []

with open("life-expectancy.csv") as data_set:
    next(data_set)
    for row in data_set:
        row = row.split(",")
        entity = row[0].strip()
        code = row[1].strip()
        year = int(row[2])
        life_expectancy = float(row[3])

        life_expectancy_values.append(life_expectancy)
        years.append(year)


        max_life = -1
        min_life = min(life_expectancy)
        avg_life = sum(life_expectancy) / len(life_expectancy)

        max_country = ""
        max_year = max(year)
        min_country = min(entity)
        min_year = min(year)

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

emaline@Emas-Macbook-Pro dougstuff % /usr/local/bin/python3 /Users/emaline/CODE/dougstuff/stuff.py

Traceback (most recent call last):
  File "/Users/emaline/CODE/dougstuff/stuff.py", line 24, in <module>
    min_life = min(life_expectancy)
               ^^^^^^^^^^^^^^^^^^^^
TypeError: 'float' object is not iterable

ChatGPT
The error you're encountering, "TypeError: 'float' object is not iterable," is because you're trying to use the min() function on a single float value (life_expectancy), which is not iterable.

I see that you want to calculate the minimum, maximum, and average life expectancies. Here's how you can modify your code to fix the issue:

python
Copy code
import os
import math
import csv

#os.chdir('dougstuff')
print()

life_expectancy_values = []
years = []

with open("life-expectancy.csv") as data_set:
    next(data_set)
    for row in data_set:
        row = row.split(",")
        entity = row[0].strip()
        code = row[1].strip()
        year = int(row[2])
        life_expectancy = float(row[3])

        life_expectancy_values.append(life_expectancy)
        years.append(year)

# Calculate statistics after the loop
max_life = max(life_expectancy_values)
min_life = min(life_expectancy_values)
avg_life = sum(life_expectancy_values) / len(life_expectancy_values)

# Find the corresponding country and year for max and min values
max_index = life_expectancy_values.index(max_life)
min_index = life_expectancy_values.index(min_life)

max_country = entity[max_index]
min_country = entity[min_index]

max_year = years[max_index]
min_year = years[min_index]

print()
year_lookup = float(input("Enter the year of interest: "))
print()

# Rest of your code goes here...
This modification moves the calculation of statistics (max_life, min_life, avg_life) outside the loop after you've collected all the data. It also finds the corresponding country and year for the maximum and minimum life expectancies. Please adapt the rest of your code accordingly.

User
Fix the whole code
ChatGPT
Certainly, I'll help you fix the code. I'll also include a more organized structure for handling statistics. Here's the modified code:

python
Copy code
import os
import csv

#os.chdir('dougstuff')
print()

life_expectancy_values = []
years = []

with open("life-expectancy.csv") as data_set:
    next(data_set)
    for row in data_set:
        row = row.split(",")
        entity = row[0].strip()
        code = row[1].strip()
        year = int(row[2])
        life_expectancy = float(row[3])

        life_expectancy_values.append(life_expectancy)
        years.append(year)

# Calculate statistics after the loop
max_life = max(life_expectancy_values)
min_life = min(life_expectancy_values)
avg_life = sum(life_expectancy_values) / len(life_expectancy_values)

# Find the corresponding country and year for max and min values
max_index = life_expectancy_values.index(max_life)
min_index = life_expectancy_values.index(min_life)

max_country = entity[max_index]
min_country = entity[min_index]

max_year = years[max_index]
min_year = years[min_index]

print()
year_lookup = float(input("Enter the year of interest: "))
print()

# Rest of your code goes here...
# The previous code didn't show how 'chosen_year' was being used, so modify accordingly.

if chosen_year == year_lookup:
    chosen_year = year_lookup
    print(f"For the year: {year_lookup}.\n")
    print(f"The average life expectancy across all countries was: {avg_life:.2f}\n")
    print(f"The max life expectancy was in {max_country} with {max_life:.2f}\n")
    print(f"The min life expectancy was in {min_country} with {min_life:.2f}\n")

    # Check if current life expectancy is greater than the overall max
    if life_expectancy > max_life:
        max_life = life_expectancy
        max_country = entity

    print()
    print(f"The overall max life expectancy is: {max_life:.2f} from {max_country} in {max_year}\n")
    print(f"The overall min life expectancy is: {min_life:.2f} from {min_country} in {min_year}\n")
Please note that I've assumed the existence of a variable chosen_year in your code, but its usage wasn't clear from the provided snippet. Please modify the code accordingly based on how you intend to use this variable. If you have more specific requirements or additional details, feel free to let me know.

User
chosen_year needs to be defined please
ChatGPT
Certainly, I can help with that. It appears that chosen_year is used to store the user-inputted year of interest. You should define it and then use it in the conditional statements. Here's the modified code:

python
Copy code
import os
import csv

#os.chdir('dougstuff')
print()

life_expectancy_values = []
years = []

with open("life-expectancy.csv") as data_set:
    next(data_set)
    for row in data_set:
        row = row.split(",")
        entity = row[0].strip()
        code = row[1].strip()
        year = int(row[2])
        life_expectancy = float(row[3])

        life_expectancy_values.append(life_expectancy)
        years.append(year)

# Calculate statistics after the loop
max_life = max(life_expectancy_values)
min_life = min(life_expectancy_values)
avg_life = sum(life_expectancy_values) / len(life_expectancy_values)

# Find the corresponding country and year for max and min values
max_index = life_expectancy_values.index(max_life)
min_index = life_expectancy_values.index(min_life)

max_country = entity[max_index]
min_country = entity[min_index]

max_year = years[max_index]
min_year = years[min_index]

print()
year_lookup = float(input("Enter the year of interest: "))
chosen_year = year_lookup  # Define chosen_year here

print()

# Rest of your code goes here...
# The previous code didn't show how 'chosen_year' was being used, so modify accordingly.

if chosen_year == year_lookup:
    print(f"For the year: {year_lookup}.\n")
    print(f"The average life expectancy across all countries was: {avg_life:.2f}\n")
    print(f"The max life expectancy was in {max_country} with {max_life:.2f}\n")
    print(f"The min life expectancy was in {min_country} with {min_life:.2f}\n")

    # Check if current life expectancy is greater than the overall max
    if life_expectancy > max_life:
        max_life = life_expectancy
        max_country = entity

    print()
    print(f"The overall max life expectancy is: {max_life:.2f} from {max_country} in {max_year}\n")
    print(f"The overall min life expectancy is: {min_life:.2f} from {min_country} in {min_year}\n")






