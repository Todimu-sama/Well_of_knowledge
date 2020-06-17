'''
Problem 2
'''
import math
import csv
import pandas as pd

output_file = [['k_value', 'Path_length', 'Error_in_Approximation']]

k_values = [2,3,4,5,6,7,8,9,10]

pi = 3.142

#function to get values of x and y coordinates' lists

def get_coordinates(k):
    x_list = []
    y_list = []
    n = 2**k
    for i in range(1, n+2):   # n+2 because we were asked to compute n+1 points
        x = math.cos((2*pi*i)/n) * 0.5
        y = math.sin((2*pi*i)/n) * 0.5
        x_list.append(x)
        y_list.append(y)
    return (x_list, y_list)

# function to calulate the path length

def path_length(x_coordinate, y_coordinate):
    total = 0
    for i in range(len(y_list)-1):
        for j in range(len(x_list)-1):
            if i == j:
                L = math.sqrt((x_list[j+1]- x_list[j])**2 + (y_list[i+1]-y_list[i])**2)
                total += L
    return round(total, 6)
       
# storing values in a list for different values of k
 
for k in k_values:
    x_list, y_list = get_coordinates(k)
    pl_value = path_length(x_list, y_list)
    error_approx = pi - pl_value
    output_file.append([k, pl_value, error_approx])

# exporting the list to a csv file

with open('Results_2.csv', 'w') as new_file:
    file_writer = csv.writer(new_file)
    for line in output_file:
        file_writer.writerow(line)
        
# converting csv file into a dataframe and displaying results

df = pd.read_csv('Results_2.csv')
print('----------------------------------------------------------')
print('              Problem 2 Results')
print('----------------------------------------------------------')
print('')
print(df)

