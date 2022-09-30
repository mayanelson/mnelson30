'''
Mason Jar: Maya Nelson and Jonathan Song
SoftDev
K06 -- Creating a dictionary of crews with duckies
2022-09-30
time spent: hour
'''

'''
DISCO:

QCC:

OPS SUMMARY:

'''

import random

import csv
jobs = []
weight = []

with open('occupations.csv') as file:
    occupations = list(csv.reader(file))
    print(occupations)
        
def numberCruncher():
    print(random.choices(jobs, k =1, weights = weight))
    
numberCruncher()
        
        
    