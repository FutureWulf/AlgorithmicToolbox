# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    # write your code here
    fractions = []

    for i in range(0, n):
        fractions.append(values[i]/weights[i])

    while capacity != 0 and len(fractions) > 0:
        best_item = fractions.index(max(fractions))

        if capacity >= weights[best_item]:
            value += values[best_item]
            capacity -= weights[best_item]

            weights.pop(best_item)
            values.pop(best_item)
            fractions.pop(best_item)
        else:
            value += (capacity * fractions[best_item])
            capacity = 0

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
