import sqlite3

def main():
    
    # Defining and manipulating database

    # Establish database connection
    conn = sqlite3.connect('COLLEGE.db')
    print('Database Connected Successfully!!')
    
    # Create a cursor
    cur = conn.cursor()

    # Create a table
    cur.execute('CREATE TABLE STUDENT\
        (RollNum INT CHECK(TYPEOF(RollNum) = "integer") PRIMARY KEY ,\
         Name VARCHAR(20) CHECK(TYPEOF(Name) = "text") NOT NULL,\
         Percentage INT CHECK(TYPEOF(Percentage) = "integer") NOT NULL\
         );')
    print('Table Created Successfully!!')
    
    # Inserting data into table
    cur.execute("INSERT INTO STUDENT VALUES (1, 'Hiten', 89);")
    cur.execute("INSERT INTO STUDENT VALUES (2, 'Muskan', 85);")
    cur.execute("INSERT INTO STUDENT VALUES (3, 'Nidhi', 78);")
    cur.execute("INSERT INTO STUDENT VALUES (4, 'Nikhil', 55);")
    cur.execute("INSERT INTO STUDENT VALUES (5, 'Deepti', 95);")
    print('Data Inserted Successfully!!')

    conn.commit()
    
    # Retrieving data from table
    print('Output of Select Queries')
    print('Retrieving roll numbers, names, and percentages of students')
    cur.execute('SELECT RollNum, Name, Percentage FROM\
    STUDENT;')
    print(cur.fetchall())
          
    print('Retrieving all attribute values of students')
    cur.execute('SELECT * FROM STUDENT;')
    print(cur.fetchall())
          
    print('Retrieving roll numbers and names of students')
    cur.execute('SELECT RollNum, Name FROM STUDENT;')
    print(cur.fetchall())
          
    print('Retrieving all attribute values of students with\
    percentage greater than 80')
    cur.execute('SELECT * FROM STUDENT WHERE Percentage > 80;')
    print(cur.fetchall())

    # Updating data of table
    cur.execute('UPDATE STUDENT \
                 SET Percentage = Percentage * 1.02 \
                 WHERE Percentage < 50;')
    print('Data Updated Successfully!!')

    # Deleting data from table
    cur.execute('DELETE FROM STUDENT WHERE RollNum = 3;')
    print('Table Data Deleted Successfully!!')
    
    # Deleting entire table
    cur.execute('DROP TABLE STUDENT')
    print('Table Deleted Successfully!!')

    # Close the connection
    conn.close()
    

if __name__ == '__main__':
  main()
