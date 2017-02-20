# Uses python3
import sys
import math

def binary_search(sorted_array, low, high, search_term):

    if high < low:
        return -1
    
    mid = math.floor(low + ((high - low) / 2))
    
    if search_term == sorted_array[mid]:
        return mid
    
    elif search_term < sorted_array[mid]:
        return binary_search(sorted_array, low, mid - 1, search_term)
    
    else:
        return binary_search(sorted_array, mid + 1, high, search_term)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    
    n = data[0]
    m = data[n + 1]
    
    sorted_array = data[1 : n + 1]
    low, high = 0, (len(sorted_array) - 1)
    
    for search_term in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(sorted_array, low, high, search_term), end = ' ')