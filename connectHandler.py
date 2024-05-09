from log import logConfiguration

import mysql.connector
import traceback
import logging.config
import time

hostname = "139.144.217.51"
dbName = "LCSATienda"
username = "lcsa"
password = "lcsa2024!2"

#Port 3306 - MariaDB

infoLog = logging.getLogger('infoLog')

def connectDB():
    connectDB = None
    try:
        infoLog.info(f"Username {username} trying to connect to {hostname}, database: {dbName}")
        connectDB = mysql.connector.connect(
            host = hostname,
            database = dbName,
            user = username,
            password = password
        )
        infoLog.info(f"Username {username} connected to {hostname}, database: {dbName}")
        return connectDB
        
    except Exception as error:
        print(f"ERROR: Wasn't possible to connect to {hostname}, error message:\n{error}")
        infoLog.error(f"Wasn't possible to connect to {hostname}, error message: {error}")
        infoLog.error(traceback.format_exc())
    return None

def closeConn(connection):
    if not connection:
        return

    try:
        connection.close()
        infoLog.info("Connection closed.")
        infoLog.info(f"User {username} successfully logged out of the database.")
    except Exception as error:
        print(f"Wasn't possible to close the session{error}")