'''
Problem 3
'''
import math
import pandas as pd
import csv

out_file = [['a_value', 't_value', 'n_value', 'f(t)', 's(t, n)', 'f(t) - s(t,n)']]
# a value is the alpha value

pi = 3.142

# Problem 3, part a

def S(t, n, T):
    total = 0
    for i in range(1, n+1):
        S = (4/pi)*(1/(2*i-1) * math.sin((2*(2*i-1)* pi * t)/T))
        total += S    
    return total

#Problem 3, part b

def f(t, T):
    if 0 < t and t < T/2:
        return 1
    elif t == T/2:
        return 0
    elif T/2 < t and t < T:
        return -1

#Problem 3, part c

# storing necessary values into a list

for alpha in [0.01, 0.25, 0.49]:
    for n_value in [1, 3, 5, 10, 30, 100]:
            t_value = 2*pi*alpha
            a = f(2*pi*alpha, 2*pi)
            b = S(2*pi*alpha, n_value, 2*pi)
            c = a - b
            out_file.append([alpha,t_value, n_value, a, b, c])
            
# exporting output file to a csv file        
    
with open('Results_3.csv', 'w') as new_file:
    file_writer = csv.writer(new_file)
    for line in out_file:
        file_writer.writerow(line)
        
# converting csv file to a data frame
        
df = pd.read_csv('Results_3.csv')

# splitting the dataframe into smaller dataframes and printing them

df_1 = df.iloc[0:6] #values of error when alpha is 0.01
df_2 = df.iloc[6:12] #values of error when alpha is 0.25
df_3 = df.iloc[12:18] #values of error when alpha is 0.49

print('----------------------------------------------------------')
print('              Problem 3 Results')
print('----------------------------------------------------------')
print('')
print(df_1)
print('                 ')
print(df_2)
print('                 ')
print(df_3)
