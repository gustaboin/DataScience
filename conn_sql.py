# Model fro create a connection

# first import pyodbc
# pyodbc is an open source Python module that makes accessing ODBC databases simple
import pyodbc

# The easiest way to install pyodbc is to use pip: python -m pip install pyodbc

# To Know wich drivers have you got
print(pyodbc.drivers())

# server credentials
server_name = "Here Server_name"
db_name = "Here database_name"
user = "user_name"
password = "password"

server = "Server=" + str(server_name)
db = "Database=" + str(db_name)
uid = "Uid=" + str(user)
pwd = "Pwd=" + str(password)

# Driver String for connection
key = f"Driver={{ODBC Driver 17 for Sql Server}};{server};{db};{uid};{pwd};"

conn = pyodbc.connect(key)

# The cursor class Enables Python scripts to use a database session to run SQL commands

cursor = conn.cursor()

# query definition
query = "SELECT * FROM TABLENAME"

# query execution

cursor.execute(query)

# Import libraries for arrays Numpy --> Numerical Python and Pandas Data panel for DataFrame

import numpy as np
import pandas as pd

# importing headers from my Sql's tables and saving like list

header = [column[0] for column in cursor.description]

# I loop through all the rows and save them in another list

row = [row for row in cursor.fetchall()]

# dataset like array
dataset = np.array(row)

# Now DataFrame = Two-dimensional, size-mutable, potentially heterogeneous tabular data.

df = pd.DataFrame(data=dataset, columns=header)

# check the data print(df)
