# Uses python3
def gcd_euclid(a, b):
    remainder = a % b

    if (b == 1) or (remainder == 1):
        return remainder

    elif remainder == 0:
        return b

    else:
         return gcd_euclid(b, remainder)


numbers = [int(x) for x in input().split()]

if numbers[0] < numbers[1]:
    a = numbers[1]
    b = numbers[0]
else:
    a = numbers[0]
    b = numbers[1]

print(gcd_euclid(a, b))
