import random

with open('krewes.txt') as file:
    contents = file.read()
    devos = contents.split("@@@")
    krewes = 
    
    
def selectDevo():
    randomCrew = randint(0,2)
    if randomCrew == 0:
        randomCrew = 7
    elif randomCrew == 1:
        randomCrew = 8
    devoList = krewes[randomCrew]

    randomDevo = randint(0,len(devoList)-1)
    return devoList[randomDevo]