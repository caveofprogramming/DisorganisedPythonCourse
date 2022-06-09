#!./venv/bin/python

temperature_f = input("Enter a temperature in Fahrenheit: ")

temperature_c = (float(temperature_f) - 32) * 0.5556

print(temperature_f + " Fahrenheit is " + str(temperature_c) + " celsius")