# Uses python3
import sys

def get_change(amount):

    coins = 0

    while amount >= 10:
        amount = amount - 10
        coins += 1
    while amount >= 5:
        amount = amount - 5
        coins += 1

    coins += amount
    return coins

amount = int(input())
print(get_change(amount))
