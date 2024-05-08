from log import infoLog

import mysql.connector
import traceback

hostname = "139.144.217.51"
dbName = "LCSATienda"
username = "lcsa"
password = "lcsa2024!2"

#Port 3306 - MariaDB


def connectDB():
    connectDB = None
    try:
        print(f"INFO: Trying to connect to {hostname}, database: {dbName}")
        infoLog.info(f"Trying to connect to {hostname}, database: {dbName}")
        connectDB = mysql.connector.connect(
            host = hostname,
            database = dbName,
            user = username,
            password = password
        )
        
    except Exception as error:
        print(f"ERROR: Wasn't possible to connect to {hostname}, error message:\n{error}")
        infoLog.error(f"Wasn't possible to connect to {hostname}, error message: {error}")
        infoLog.error(traceback.format_exc())
    return connectDB

def closeConn(connection):
    if not connection:
        return

    try:
        connection.close()
        infoLog.info("Connection closed.")
        print(f"User {username} successfully logged out of the database.\n")
    except Exception as error:
        print(f"Wasn't possible to close the session{error}")