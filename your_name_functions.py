#modify this module to include the function definitions
#Developed by :   Kethireddy Sai Vamshi Reddy
import sqlite3
import os
def create_database_file(file_name):
    try:
        conn = sqlite3.connect(file_name)
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    else:
        print('Created the database file.')
        return conn
    
def create_rep_table(database_connection):
    try:
        cursor = database_connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS rep (
                rep_num CHAR(2) PRIMARY KEY,
                last_name CHAR(15),
                first_name CHAR(15),
                street CHAR(15),
                city CHAR(15),
                state CHAR(2),
                zip CHAR(5),
                commission DECIMAL(7, 2),
                rate DECIMAL(3, 2)
            );
        ''')
        rep_data = [
            ('20', 'Vamshi', 'Sai', '624 Randall', 'Grove', 'FL', '33321', 20542.50, 0.05),
            ('35', 'Hull', 'Richard', '532 Jackson', 'Sheldon', 'FL', '33553', 39216.00, 0.07),
            ('65', 'Perez', 'Juan', '1626 Taylor', 'Fillmore', 'FL', '33336', 23487.00, 0.05)
        ]
        cursor.executemany('INSERT INTO rep VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', rep_data)
        database_connection.commit()
        print("Rep table created and data inserted successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Integrity error: {e}")
    except sqlite3.Error as e:
        print(f"Error creating rep table: {e}")

def create_customer_table(database_connectiion):
    #use the connection object to create the database table
    #Create a function that will create the customer table and add the data to it.
    # Use the data in sql_commands.txt to help you with it.
    pass
def insert_a_customer_record(database_connectiion):
    #Create a function that prompts the user for a rep number. 
    # If the result is not empty, display the first record.
    pass
def query_rep_table(database_connection):
    #Create a function that prompts the user for a rep number. 
    # If the result is not empty, display the first record.
    pass
def update_rep_table(database_connection):
    #Create a function that prompts the user for a rep number.  
    # Then use the rep number to update the rep commission if it is in the [0.0 to 0.20]  range
    pass
def delete_customer_record(database_connection):
    # Create a function that prompts the user for a customer number.  
    # if the customer number exists, confirm for deletion and 
    # then and delete then delete that customer 
    pass
def delete_database(file_name, database_connection):
    # Create a function that deletes the database.  Verify that the file exists. 
    # Close the connection.  Then confirm the user really wants to delete the file,  Then delete the file.
    pass