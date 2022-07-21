#!./venv/bin/python


def main():
    for x in range(0, 256):
        print(f"{x:03} {x:08b} {x:02x}")

    print()

    print("{:06x}".format(0x123456))
    print("{:06x}".format(0x123456 & 0xFF00FF))


if __name__ == "__main__":  
    main()
