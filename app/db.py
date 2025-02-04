# Put dataframe/table in sqlite3 DB (temp for now)
import sqlite3
import pandas as pd

def save_to_db(df, table_name):
    """
    Save pandas dataframe to database
    """

    # Path to your SQLite database file
    db_file = 'app/auctions.db'

    try: 
        # Connect to the SQLite database
        conn = sqlite3.connect(db_file)

        # Put the DataFrame into the SQLite database
        df.to_sql(table_name, conn, if_exists='replace', index=False)

        # Commit the changes and close the connection
        conn.commit()
    
    except sqlite3.Error as error:
        print("Error! Failed to execute sqlite3 query", error)

    finally:
        if conn:
            conn.close()

def get_dataframe_from_db(table_name):
    """
    Get data from db and put back in a pandas dataframe
    """
    print('get_dataframe_from_db')
    # Path to your SQLite database file
    db_file = 'app/auctions.db'

    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_file)

        # SQL query to select data from the database table
        query = f"SELECT * FROM {table_name}"

        # Read data from the database into a Pandas DataFrame
        df = pd.read_sql_query(query, conn)

        # Print the DataFrame to verify the data
        #print(df)

        return df


    except sqlite3.Error as error:
        print("Error! Failed to execute sqlite3 query", error)

    finally:
        if conn:
            # Close the database connection
            print('closing db connection...')
            conn.close()


def get_all_tables_from_db():
    """ Get and return all table names from the DB """

    db_file = 'app/auctions.db'
    try:
        conn = sqlite3.connect(db_file)
        sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""
        cursor = conn.cursor()
        cursor.execute(sql_query)

        return cursor.fetchall()

    except sqlite3.Error as error:
        print("Error! Failed to execute sqlite3 query", error)

    finally:
        print('run finally')
        if conn:
            conn.close()


def update_db_table(df, table_name):
    db_file = 'app/auctions.db'

    # Update the DataFrame as needed
    # For example, you can add a new column or modify existing data
    # df['new_column'] = 'new_value'

    try:
        # Connect to the SQLite database again
        conn = sqlite3.connect(db_file)

        # Write the updated DataFrame back to the database
        df.to_sql(table_name, conn, if_exists='replace', index=False)

        # Commit the changes and close the connection
        conn.commit()
    
    except sqlite3.Error as error:
        print("Error! Failed to execute sqlite3 query", error)
    
    finally:
        if conn:
            conn.close()



def filter_by_time(table_name, time):
    """
    Get data from db and put back in a pandas dataframe
    """
    # Path to your SQLite database file
    db_file = 'app/auctions.db'

    try: 
        # Connect to the SQLite database
        conn = sqlite3.connect(db_file)

        # SQL query to select auctions where time is less than xxx
        query = f"SELECT * FROM {table_name} WHERE AUCTION TIME < {time}"

        # Read data from the database into a Pandas DataFrame
        df = pd.read_sql_query(query, conn)

        # Print the DataFrame to verify the data
        print(df)

        return df


    except sqlite3.Error as error:
        print("Error! Failed to execute sqlite3 query", error)

    finally:
        if conn:
            # Close the database connection
            conn.close()


"""
db_tables = get_all_tables_from_db()
print('db_tables', db_tables)
for table_name in db_tables:
    # Grab the (only) table name in the tuple
    print(table_name[0])
    print(type(table_name[0]))
    df = get_dataframe_from_db(table_name[0])
"""