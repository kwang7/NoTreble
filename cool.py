'''
Kelly Wang
SoftDev1 pd7
HW09--No Treble
2017-10-16
'''
import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f = "discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#create peeps table
command = "CREATE TABLE peeps ( name TEXT , age INTEGER , id INTEGER )"
c.execute(command)

#create courses table
command = "CREATE TABLE courses ( code TEXT , mark INTEGER , id INTEGER )"
c.execute(command)

#read peeps.csv and put it into the table
peepz = csv.DictReader(open("peeps.csv"))
for row in peepz:
    #print row
    name = row['name']
    age = row["age"]
    iD = row['id']
    command = "INSERT INTO peepz VALUES( name , age, iD )"
    c.execute(command)
    
#read courses.csv and put it into the table
coursez = csv.DictReader(open("courses.csv"))
for row in coursez:
    #print row
    code = row['code']
    mark = row['mark']
    iD = row['id']
    command = "INSERT INTO coursez ( code , mark . iD )"
    c.execute(command)

db.commit() #save changes
db.close()  #close database
