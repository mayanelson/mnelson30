'''
Mason Jar: Maya Nelson and Jonathan Song
SoftDev
K06 -- Randomizing the occupations in a csv file
2022-09-30
time spent: 2 hours
'''

'''
DISCO:
* A built in csv reader exists!! Woah!!
* Random.choices takes a list of weights that returns items in a list based on their percentage.
* You can't loop through a file twice. Use .seek() to 'reset' it.
* You can't typecast something with a decimal as an int.
QCC:
* Why can't you loop through rows in a file multiple times?
* Is there any shorter way to find how many rows are in a file without looping through?
OPS SUMMARY: Uses the csv reader to loop through the rows in a file to find the num of rows.
Then reads through again, adding each occupation to a jobs list and each percentage to weights.
Uses random.choices to select a random value given the weights.
'''

import random

from csv import reader

jobs = []
weight = []

with open('occupations.csv','r') as file:
    contents = reader(file)
    count = 0
    rcount = 0
    for row in contents: #get the amount of rows to ignore the last line
        rcount +=1
    file.seek(0) # resets reader back to beginning
    for row in contents:
        if count != 0 and count != rcount-1:
            jobs.append(row[0])
            weight.append(int(float(row[1])*10)) #typecasts as float rather than string, then coverts to int
        count+=1
    
        
print(random.choices(jobs, weights = weight)) #random.choices takes weight into account for each value
    
        
