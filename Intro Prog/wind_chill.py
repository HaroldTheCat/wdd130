
import math

# The Math recal!
def WC(temp, wi_sp):
    # Calculating Wind Chill Index 
    wci = 13.12 + 0.6215 * temp - 11.37 * math.pow(wi_sp, 0.16) + \
        0.3965 * temp * math.pow(wi_sp, 0.16)
    return wci

# C to F function
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# What temprature do you want to use the correct answer is Celsius. 
temp_scale = input("Choose temperature scale (C for Celsius, F for Fahrenheit): ").upper()

# Why was subjected to this nightmare? F vs C calulation 
if temp_scale == 'C':
    temp_celsius = float(input("Enter the Air Temperature (in Celsius): "))
elif temp_scale == 'F':
    temp_fahrenheit = float(input("Enter the Air Temperature (in Fahrenheit): "))
    temp_celsius = (temp_fahrenheit - 32) * 5/9
else:
    print("Invalid temperature scale. Please choose C or F.")
    exit()

# What is the wind speed!
wi_sp = float(input("Enter the Wind Speed (in km/h): "))

# Recall for your maths!
wci_result = WC(temp_celsius, wi_sp)
print("The Wind Chill Index is", int(round(wci_result)))
