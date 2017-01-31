# Uses python3
import sys


def gcd_euclid(a, b):

    remainder = a % b

    if b == 1 or remainder == 1:
        return 1

    elif remainder == 0:
        return b

    else:
        gcd_euclid(b, remainder)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_euclid(a, b))
