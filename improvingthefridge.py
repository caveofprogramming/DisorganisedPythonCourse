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

temperature = float(temperature)

F_BROKEN = "Fridge broken"
F_OK = "OK"
F_WARM = "Too warm"
F_COLD = "Too cold"

status = F_BROKEN

if temperature < 0:
    status = F_COLD
elif temperature < 4:
    status = F_OK
elif temperature < 6:
    status = F_WARM

print(status)




