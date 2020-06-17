'''
Problem 1
'''
import math

# Problem 1, part a

A = [] # contains all x coordinates

B = [] #contains all y coordinates

pi= 3.142

test_length = None

def path_length(x_coordinate, y_coordinate):
    total = 0
    for i in range(len(B)-1):
        for j in range(len(A)-1):
            if i == j:
                L = math.sqrt((A[j+1]- A[j])**2 + (B[i+1]-B[i])**2)
                total += L
    return round(total, 6)

pl_value = path_length(A, B)

# Problem 1, part b

def test_path_length(test_length):
    if test_length == pl_value:
        print('Correct value')
    elif test_length != pl_value:
        print('Wrong Value')

print('Problem one executed successfully')