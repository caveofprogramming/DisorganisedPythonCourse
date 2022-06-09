#!./venv/bin/python

# Exercise: The Fridge

"""
Get the user to input a temperature in celsius.

If the temperature is less than 0 degrees, output "Too cold."
If it's between 0 and 4 degrees, output "OK"
If it's between 4 and 6 degrees, output "Too warm"
If over 6 degrees, then output "Fridge broken"
"""

temperature = input("Enter fridge temperature > ")

if float(temperature) < 0:
    print("Too cold")
elif float(temperature) < 4:
    print("OK")
elif float(temperature) < 6:
    print("Too warm")
else:
    print("Fridge broken")




