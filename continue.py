#!./venv/bin/python

for loop_index in range(0, 5):
    print("Loop index is: " + str(loop_index))

    stop = input("Should the loop continue? y/n > ")

    if stop == "y":
        continue

    print("Still looping")

print("Program finished")