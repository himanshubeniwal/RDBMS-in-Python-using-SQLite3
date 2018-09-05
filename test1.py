import sqlite3
# Connecting to database 
def connecting():
    conn = sqlite3.connect('test.db')
    print ("Opened database successfully")
    conn.close()

def creating_table():
    conn = sqlite3.connect('test.db')
    print ("Opened database successfully")
    conn.execute('''CREATE TABLE COMPANY
             (ID INT PRIMARY KEY     NOT NULL,
             NAME           TEXT    NOT NULL,
             AGE            INT     NOT NULL,
             ADDRESS        CHAR(50),
             SALARY         REAL)''')
    print ("Table created successfully")

def inserting_values():
    conn = sqlite3.connect('test.db')
    print("Inserting values in database!")
    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (1, 'Himanshu Beniwal', 19, 'Rohtak', 200000.00 )")
    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (2, 'Sumit Semwal', 20, 'Rudraprayag', 150000.00 )")
    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (3, 'Jagdeepak Rawat', 23, 'Gairsan', 20000.00 )")
    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (4, 'Ajay Kathait', 20, 'Gauchar', 65000.00 )")
    conn.commit()
    print ("Records created successfully")
    conn.close()

def selecting():
    conn = sqlite3.connect('test.db')
    print( "Opened database successfully")
    cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
    for row in cursor:
       print( "ID = ", row[0])
       print( "NAME = ", row[1])
       print ("ADDRESS = ", row[2])
       print ("SALARY = ", row[3], "\n")
    print("Operation done successfully")
    conn.close()

def updating():
    conn = sqlite3.connect('test.db')
    print( "Opened database successfully")
    conn.execute("UPDATE COMPANY set SALARY = 900000.00 where ID = 1")
    conn.commit()
    print ("Total number of rows updated :", conn.total_changes)
    ### Showing the rest of table ### 
    cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
    for row in cursor:
       print( "ID = ", row[0])
       print( "NAME = ", row[1])
       print( "ADDRESS = ", row[2])
       print( "SALARY = ", row[3], "\n")
    print( "Operation done successfully")
    conn.close()

def deleting_table():
    con = sqlite3.connect("test.db")
    con.execute("DROP TABLE COMPANY")
    con.commit()
    con.close()

def deleting_item():
    conn = sqlite3.connect('test.db')
    print ("Opened database successfully")
    conn.execute("DELETE from COMPANY where ID = 2;")
    conn.commit()
    print ("Total number of rows deleted :", conn.total_changes)
    #### showing table again #######
    cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
    for row in cursor:
       print ("ID = ", row[0])
       print ("NAME = ", row[1])
       print ("ADDRESS = ", row[2])
       print ("SALARY = ", row[3], "\n")
    print( "Operation done successfully")
    conn.close()
    
def inserting_item_back():
    conn= sqlite3.connect("test.db")
    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (2, 'Sumit Semwal', 20, 'Rudraprayag', 150000.00 )")
    conn.commit()
    cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
    for row in cursor:
       print ("ID = ", row[0])
       print ("NAME = ", row[1])
       print ("ADDRESS = ", row[2])
       print ("SALARY = ", row[3], "\n")
    conn.close()
'''
print("\t\nCreating Table Now ~!~!~!~!~!")
creating_table()
print("\t\nInserting values in table Now ~!~!~!~!~!")
inserting_values()
print("\t\nSelecting Table Now ~!~!~!~!~!")
selecting()
print("\t\nUpdating Table Now ~!~!~!~!~!")
updating()
print("\t\nDeleting Item Now ~!~!~!~!~!")
deleting_item()
print("\t\nInserting Item Back Now ~!~!~!~!~!")
inserting_item_back()
'''
'''    EXPORTING DATA INTO CSV FILES!!!!! 
conn = sqlite3.connect('test.db')
print( "Opened database successfully")
cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
with open("test.csv",'w') as f:
    for row in cursor:
       f.writelines(row)
print("Operation done successfully")
conn.close()
'''
############### MANUAL ###########33
'''
connecting ~~~~ creating connection
creating_table ~~~~~ to create a table 
inserting_values~~~~~ insert values 
selecting ~~~~~~~~~~~~ show values in table 
updating~~~~~~~~~~~~ to update any value 
deleting_item ~~~~ to delete any specific item
inserting_item~~~~ insert the item back in table 
deleting_table ~~~~ DONT FORGET TO delete full table when creating table again
'''
