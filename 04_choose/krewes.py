
'''
ZEM ZEM :: Maya Nelson, Ziying Jian, Elizabeth Paperno
SoftDev
K04 -- Creating a dictionary of crews
2022-09-22
time spent: <elapsed time in hours, rounded to nearest tenth>
'''

'''
DISCO:
* To import a statement, use from... import...
* randint() is an imported function to generate a random integer
* The conditions for randint() are both inclusive
* Random number should be 2, 7, or 8

QCC:
* How do we get the full names of all thinkerens in all periods?
* Why is our current code not working?

OPS SUMMARY:
'''

from random import randint

krewes = {2:['a', 'b', 'c'], 7:['d', 'e', 'f'], 8:['g', 'h', 'i']}

def selectDevo():
    randomCrew = randint(0,2)
    if randomCrew == 0:
        randomCrew = 7
    elif randomCrew == 1:
        randomCrew = 8
    devoList = krewes[randomCrew]

    randomDevo = randint(0,len(devoList)-1)
    return devoList[randomDevo]

for i in range(100):
    print(selectDevo())
