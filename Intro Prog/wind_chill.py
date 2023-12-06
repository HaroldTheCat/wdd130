
import math


def WC(temp, wi_sp):
    
    wci = 13.12 + 0.6215 * temp - 11.37 * math.pow(wi_sp, 0.16) + \
        0.3965 * temp * math.pow(wi_sp, 0.16)
    return wci


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


temp_scale = input("Choose temperature scale (C for Celsius, F for Fahrenheit): ").upper()

# Taking the Air Temperature (Ta) as input
if temp_scale == 'C':
    temp_celsius = float(input("Enter the Air Temperature (in Celsius): "))
elif temp_scale == 'F':
    temp_fahrenheit = float(input("Enter the Air Temperature (in Fahrenheit): "))
    temp_celsius = (temp_fahrenheit - 32) * 5/9
else:
    print("Invalid temperature scale. Please choose C or F.")
    exit()


for wind_speed in range(5, 61, 5):
    wind_speed_kph = wind_speed * 1.60934
    
   
    wci_result = WC(temp_celsius, wind_speed_kph)
    print("Wind Speed: {} mph, Wind Chill Index: {:.2f}".format(wind_speed, wci_result))

