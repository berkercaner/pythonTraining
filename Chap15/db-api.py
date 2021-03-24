 #!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
"""
    every database engine has its own interface, requirements so no single interface
    will ever serve all of them equally
    so python db-api won't be exactly same for every database system
"""

"""
    python ships with sqlite: fully functional, cross platform, database system
                                that suitable for many online and mobile applications
"""

import sqlite3

def main():
    #first thing to do is to connect to database
    print('connect')
    #this line return a database handle so we can use it to interface with the database
    db = sqlite3.connect('db-api.db') #we can give any name 
    #grabbing a cursor allow us to keep track where we are in the database as 
    #we run database commands
    cur = db.cursor()
    print('create')
    #executing SQL->
    cur.execute("DROP TABLE IF EXISTS test")
    cur.execute("""
        CREATE TABLE test (
            id INTEGER PRIMARY KEY, string TEXT, number INTEGER
        )
        """)
    print('insert row')
    #inserting multiple rows
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('one', 1)
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('two', 2)
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('three', 3)
        """)
    print('commit')
    #and we commit 
    db.commit()
    print('count')
    #if we want number of rows in the table we use "SELECT COUNT(*) command"
    cur.execute("SELECT COUNT(*) FROM test")
    #and we fetchone() from the cursor after the SQL command
    #that will return a row with one element in it that will have the count of the number of rows
    count = cur.fetchone()[0]
    print('there are {} rows in the table.'.format(count))
    print('read')
    for row in cur.execute("SELECT * FROM test"): #we can print the rows in the table
        print(row)
    print('drop')
    cur.execute("DROP TABLE test")
    #and we close
    print('close')
    db.close()

if __name__ == '__main__': main()
