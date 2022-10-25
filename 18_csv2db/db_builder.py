# Whatever: Elizabeth, Anthony, Maya
#SoftDev
#K18 :: SQLITE3 BASICS
#2022-10-25

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

def popTable(filename):
    with open(filename) as f:
        csvfile = csv.reader(f)
        titles = next(csvfile)

        tblname = filename.split(".")[0]
        c.execute(f"DROP TABLE IF EXISTS {tblname}")
        c.execute(f"CREATE TABLE {tblname}({titles[0]} TEXT,{titles[1]} INTEGER, {titles[2]} INTEGER)")

        for row in csvfile:
            c.execute(f"INSERT INTO {tblname} VALUES (\"{row[0]}\", {row[1]}, {row[2]})")


if __name__ == "__main__":
    csvfiles = ["courses.csv","students.csv"]

    for f in csvfiles:
        popTable(f)
        tablename=f.split(".")[0]
        c.execute(f"SELECT * FROM {tablename}")
    

#==========================================================

db.commit() #save changes
db.close()  #close database


