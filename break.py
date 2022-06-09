#!./venv/bin/python

for loop_index in range(0, 5):
    print("Loop index is: " + str(loop_index))

    stop = input("Should the loop stop? y/n > ")

    if stop == "y":
        break

    print("Still looping")

print("Program finished")