# Uses python3
import sys

def get_majority_element(input_array, length):

    occurances = {}
    
    for i in range(0, length):
        key = input_array[i] 
    
        if key in occurances:
            occurances[key] += 1
            
        else:
            occurances[key] = 1
    
    return any(value > (length / 2) for value in occurances.values())
   
    
if __name__ == '__main__':

    input = sys.stdin.read()
    length, *input_array = list(map(int, input.split()))
    
    if get_majority_element(input_array, length):
        print(1)

    else:
        print(0)