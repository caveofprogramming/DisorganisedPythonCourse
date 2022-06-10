#!./venv/bin/python

def calculate_box_volume(width, length, height):
    return width * length * height

def greet():
    return "Hello there"

def main():
    greeting = greet()
    print(greeting)

    box_volume = calculate_box_volume(2, 3.5, 4);
    print(box_volume)

    print(calculate_box_volume(2, 3.5, 4))

main()