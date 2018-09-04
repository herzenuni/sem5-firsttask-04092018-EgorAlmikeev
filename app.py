import sys

usage = """
USAGE:
first arg: digit from 0 to 9
second arg: string bin, oct, hex
"""


def is_int(digit):
    try:
        digit = int(digit)
    except:
        return False
    return True


def print_digit_word(digit):
    if digit == 0:
        print("\nЭто нуль")
    elif digit == 1:
        print("\nЭто одын")
    elif digit == 2:
        print("\nЭто два")
    elif digit == 3:
        print("\nЭто три")
    elif digit == 4:
        print("\nЭто четыре")
    elif digit == 5:
        print("\nЭто пятb")
    elif digit == 6:
        print("\nЭто шестb")
    elif digit == 7:
        print("\nЭто семb")
    elif digit == 8:
        print("\nЭто восемb")
    elif digit == 9:
        print("\nЭто девятb")
    else:
        print("\nНет такой цифры")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(usage)
        exit(0)

    if not is_int(sys.argv[1]):
        print("\n" + sys.argv[1] + " – не цифра")
        exit(0)

    sys.argv[1] = int(sys.argv[1])

    if len(sys.argv) == 2:
        print_digit_word(int(sys.argv[1]))
    elif len(sys.argv) == 3:
        if sys.argv[2] not in ("bin", "oct", "hex"):
            print("\nВторой аргумент должен быть bin, oct, или hex")
            exit(0)
        if sys.argv[2] == "bin":
            print(str(bin(sys.argv[1]))[2:])
        elif sys.argv[2] == "oct":
            print(str(oct(sys.argv[1]))[2:])
        elif sys.argv[2] == "hex":
            print(str(hex(sys.argv[1]))[2:])
