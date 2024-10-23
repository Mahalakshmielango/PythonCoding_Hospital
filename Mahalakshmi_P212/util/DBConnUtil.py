# util/DBConnUtil.py

import pyodbc
#from util.DBPropertyUtil import DBPropertyUtil

class DBConnUtil:
    connection = None

    @staticmethod
    def get_connection():
        """
        Establishes and returns a database connection using the connection string from DBPropertyUtil.
        """
        if DBConnUtil.connection is None:

            try:
                # You need to configure the correct connection string based on your SQL Server setup
                server = r'DESKTOP-AAMRPRI\SQLEXPRESS'  # SQL Server instance
                database = 'hospital'  # Replace with your database name
                connection_string = (
                    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                    f'SERVER={server};'
                    f'DATABASE={database};'
                    f'Trusted_Connection=yes;'
                )

                DBConnUtil.connection = pyodbc.connect(connection_string)
                print("Database connection established successfully.")

            except pyodbc.Error as e:
                print(f"Error establishing database connection: {e}")
                raise
        return DBConnUtil.connection
