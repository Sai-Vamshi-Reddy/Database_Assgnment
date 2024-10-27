#modify this module to write code for the user interface
import Kethireddy_SaiVamshiReddy_functions as functions 
connection = None 
while True:
    prompt = """
            B to create the database file
            P to create rep table
            S to create customer table
            I to insert a customer record
            R to query the Rep table
            U to update the rep table
            D to delete a customer record
            X to delete the database
            Q to quit the application
            """
    choice = input(prompt).strip().upper()  

    if choice in ('B', 'b'):
        file_name = input('Enter the database file name: ')
        connection = functions.create_database_file(file_name)

   
    elif choice in ('P', 'p'):
        if connection:
            functions.create_rep_table(connection)
        else:
            print("Error: No active database connection. Please create or open a database first.")

   
    elif choice in ('S', 's'):
        if connection:
            functions.create_customer_table(connection)
        else:
            print("Error: No active database connection. Please create or open a database first.")

    
    elif choice in ('I', 'i'):
        if connection:
            functions.insert_a_customer_record(connection)
        else:
            print("Error: No active database connection. Please create or open a database first.")

    
    elif choice in ('R', 'r'):
        if connection:
            functions.query_rep_table(connection)
        else:
            print("Error: No active database connection. Please create or open a database first.")

    
    elif choice in ('U', 'u'):
        if connection:
            functions.update_rep_table(connection)
        else:
            print("Error: No active database connection. Please create or open a database first.")

    
    elif choice in ('D', 'd'):
        if connection:
            functions.delete_customer_record(connection)
        else:
            print("Error: No active database connection. Please create or open a database first.")

    
    elif choice in ('X', 'x'):
        if connection:
            file_name = input("Enter the database file name to delete: ")
            functions.delete_database(file_name, connection)
            connection = None
        else:
            print("Error: No active database connection. Please create or open a database first.")

   
    elif choice in ('Q', 'q'):
        if connection:
            connection.close()
        print("Exiting the application.")
        break

    else:
        print("Invalid selection. Please choose a valid option.")

    
