import sqlite3

# Ordinary DB initialisation
# textDB = sqlite3.connect("testDB.db")

# Create DB in RAM
textDB = sqlite3.connect(":memory:")

# Cursor creation
curs = textDB.cursor()

#Except if DB exists
try:
    curs.execute("""CREATE TABLE info (name VARCAR(20) PRIMARY KEY, count INT, val FLOAT)""")
except:
    pass

#Manual insert
curs.execute("""INSERT INTO info VALUES("first", 6, 2.2)""")
curs.execute("""INSERT INTO info VALUES("second", 8, 1.7)""")
curs.execute("""INSERT INTO info VALUES("third", 88, 1.9)""")

#Create placeholder and use it to insert data
ins = "INSERT INTO info (name, count, val) VALUES(?,?,?)"

curs.execute(ins, ("forth", 3, 3.3))

#Print all content of DB
curs.execute("SELECT * FROM info")

rows = curs.fetchall()

print(rows)

#Order by val
curs.execute("SELECT * FROM info ORDER BY val")

print(curs.fetchall())
