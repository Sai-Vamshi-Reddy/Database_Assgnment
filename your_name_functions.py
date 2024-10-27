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

def create_customer_table(database_connection):
    try:
        cursor = database_connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customer (
                customer_num CHAR(3) PRIMARY KEY,
                customer_name CHAR(35) NOT NULL,
                street CHAR(15),
                city CHAR(15),
                state CHAR(2),
                zip CHAR(5),
                balance DECIMAL(8, 2),
                credit_limit DECIMAL(8, 2),
                rep_num CHAR(2),
                FOREIGN KEY (rep_num) REFERENCES rep (rep_num)
            );
        ''')
        customer_data = [
                 ('148','Al''s Appliance and Sport','2837 Greenway','Fillmore','FL','33336',6550.00,7500.00,'20'),
                ('282','Brookings Direct','3827 Devon','Grove','FL','33321',431.50,10000.00,'35'),
                ('356','Ferguson''s','382  Wildwood','Northfield','FL','33146',5785.00,7500.00,'65'),
                ('408','The Everything Shop','1828 Raven','Crystal','FL','33503',5285.25,5000.00,'35'),
                ('462','Bargains Galore','3829  Central','Grove','FL','33321',3412.00,10000.00,'65'),
                ('524','Kline''s','838 Ridgeland','Fillmore','FL','33336',12762.00,15000.00,'20'),
                ('608','Johnson''s Department Store','372  Oxford','Sheldon','FL','33553',2106.00,10000.00,'65'),
                ('687','Lee''s Sport and Appliance','282 Evergreen','Altonville','FL','32543',2851.00,5000.00,'35'),
                ('725','Deerfield''s Four Seasons','282 Columbia','Sheldon','FL','33553',248.00,7500.00,'35')
            #
        ]
        cursor.executemany('INSERT INTO customer VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', customer_data)
        database_connection.commit()
        print("Customer table created and data inserted successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Integrity error: {e}")
    except sqlite3.Error as e:
        print(f"Error creating customer table: {e}")


def insert_a_customer_record(database_connection):
    try:
        customer_num = input("Enter customer number: ").strip()
        customer_name = input("Enter customer name: ").strip()
        street = input("Enter street: ").strip()
        city = input("Enter city: ").strip()
        state = input("Enter state: ").strip()
        zip_code = input("Enter ZIP code: ").strip()
        try:
            balance = float(input("Enter balance: "))
            credit_limit = float(input("Enter credit limit: "))
        except ValueError:
            print("Invalid input for balance or credit limit. Please enter a numeric value.")
            return
        rep_num = input("Enter rep number: ").strip()

        cursor = database_connection.cursor()
        cursor.execute('INSERT INTO customer VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', 
                       (customer_num, customer_name, street, city, state, zip_code, balance, credit_limit, rep_num))
        database_connection.commit()
        print("Customer record inserted successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Integrity error: {e}")
    except sqlite3.Error as e:
        print(f"Error inserting customer record: {e}")

def query_rep_table(database_connection):
    rep_num = input("Enter the rep number to query: ").strip()
    try:
        cursor = database_connection.cursor()
        cursor.execute('SELECT * FROM rep WHERE rep_num = ?', (rep_num,))
        record = cursor.fetchone()
        if record:
            print("Record found:", record)
        else:
            print("No record found with that rep number.")
    except sqlite3.Error as e:
        print(f"Error querying rep table: {e}")

def update_rep_table(database_connection):
    try:
        rep_num = input("Enter rep number to update commission: ").strip()
        try:
            new_commission = float(input("Enter new commission (0.0 to 0.20): "))
            if not (0.0 <= new_commission <= 0.20):
                print("Commission out of range. Must be between 0.0 and 0.20.")
                return
        except ValueError:
            print("Invalid input for commission. Please enter a decimal value.")
            return

        cursor = database_connection.cursor()
        cursor.execute('UPDATE rep SET commission = ? WHERE rep_num = ?', (new_commission, rep_num))
        database_connection.commit()
        print("Commission updated successfully.")
    except sqlite3.Error as e:
        print(f"Error updating rep commission: {e}")
    try:
        cursor = database_connection.cursor()
        cursor.execute('SELECT * FROM rep WHERE rep_num = ?', (rep_num,))
        record = cursor.fetchone()
        if record:
            print("Updated record:", record)
        else:
            print("No record found with that rep number.")
    except sqlite3.Error as e:
        print(f"Error querying rep table: {e}")

def delete_customer_record(database_connection):
    # Create a function that prompts the user for a customer number.  
    # if the customer number exists, confirm for deletion and 
    # then and delete then delete that customer 
    pass
def delete_database(file_name, database_connection):
    # Create a function that deletes the database.  Verify that the file exists. 
    # Close the connection.  Then confirm the user really wants to delete the file,  Then delete the file.
    pass

def print_all_rep_data(database_connection):
    try:
        cursor = database_connection.cursor()
        cursor.execute("SELECT * FROM rep")
        records = cursor.fetchall()
        if records:
            print("All Rep Records:")
            for record in records:
                print(record)
        else:
            print("No records found in the rep table.")
    except sqlite3.Error as e:
        print(f"Error retrieving data from rep table: {e}")


def print_all_customer_data(database_connection):
    try:
        cursor = database_connection.cursor()
        cursor.execute("SELECT * FROM customer")
        records = cursor.fetchall()
        if records:
            print("All Customer Records:")
            for record in records:
                print(record)
        else:
            print("No records found in the customer table.")
    except sqlite3.Error as e:
        print(f"Error retrieving data from customer table: {e}")
