'''
Maya Nelson and Jonathan Song
SoftDev
K05 -- Creating a dictionary of crews with duckies
2022-09-29
time spent: 1 hour
'''

'''
DISCO:
* Some names have spaces in them...
*

QCC:
* How do we get the ducky names?
* Are we supposed to make a new dictionary or modify the old?

OPS SUMMARY:
Splits txt file into individual devo information, loops through krewes to find that devo and modifies name
by adding the ducky name next to it. The selectDevo() function finds that devo, splits it into devo and
ducky, and returns all needed information.
'''

from random import randint

krewes = {2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY"],
 7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"], 
 8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "wanying"]
 }

with open('krewes.txt') as file:
    contents = file.read()
    devos = contents.split("@@@")
    for i in range(len(devos)):
        devo = devos[i].split("$$$")
        devolist = krewes[int(devo[0])]
        for j in range(len(devolist)):
            if devolist[j] == devo[1]:
                devolist[j] += "  " + devo[2]
        krewes[int(devo[0])] = devolist
                
    
def selectDevo():
    randomCrew = randint(0,2)
    if randomCrew == 0:
        randomCrew = 7
    elif randomCrew == 1:
        randomCrew = 8
    devoList = krewes[randomCrew]

    randomDevo = randint(0,len(devoList)-1)
    devothing = devoList[randomDevo].split("  ")
    print("Name:" + devothing[0] + " Period: " + str(randomCrew))
    if len(devothing) > 1:
        print(" Ducky:" + devothing[1])
 

print(krewes)
for i in range(10):
    selectDevo()
