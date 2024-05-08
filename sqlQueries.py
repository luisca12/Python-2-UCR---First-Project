from connectHandler import connectDB, closeConn,username,hostname
from log import infoLog

import traceback
import os
import datetime

def getAllPurchases():
    orderID = int
    userID = int
    # Step 1: This is to obtain all the purchases registered
    sqlQuery = "SELECT * FROM Pedidos"
    # The abpve query will return something like this
    #[
    ##    (1, 5, datetime.date, 'delivered', decimal.Decimal(1500)),
    ##    (1, 5, datetime.date, 'delivered', decimal.Decimal(1500))
    # ]

    # Step 2: Obtain the details of a specific purchase
    sqlQuery1 = f"SELECT * FROM Detalles_de_Pedido WHERE OrderID = {orderID}"
    # The above query will return something like this
    [
        (1, 5, 5, 10, 50),
        (1, 3, 5, 10, 50)
    ]

    # Step 3: To obtain the informaion of a specific product 
    sqlQuery2 = f"SELECT Nombre FROM Productos WHERE ProductID = {orderID}"

    # Step 4: Bonus
    sqlQuery3 = f"SELECT * FROM Usuarios WHERE userID = {userID}"

def makePurchase():
    userID = int
    price = int

    # Step 1: Get all the users and choose the user
    sqlQuery = "SELECT * FROM Usuarios"
    # This will query and return the following
    [
        (1, 'Name', 'Surname', 'email', datetime.date, 'Country')
    ]

    # Step 2: The customer chooses all the products and the amount
    sqlQuery1 = "SELECT * FROM Productos"
    [
        (1, 'Product', 'Descount', 30, 100)
    ]

    # Step 3: Make the purchase
    sqlQuery2 = "INSERT INTO Pedidos (UserID, Fecha_de_pedido, Estado, Total) VALUES "\
        f"( {userID}, '2024-04-29', 'creado', {price} )"
    
    # Step 4: 
    sqlQuery3 = "INSERT INTO Detalles_de_pedido (OderID, ProductID, Cantidad, Precio_unitario, subtotal)" \
        f"VALUES ({purchaseID}, {productID}, {amountProducts}, {price}, {subtotal})"

def addUserDB(name, surname, email, birthdate, country):
    # Step 1:
    connection = connectDB
    if not connection:
        return False
    tableName = "Usuarios"
    sqlQuery = f"INSERT INTO {tableName} (Nombre, Apellidos, Email, Fecha_de_nacimiento, Pais)" \
        f"VALUES ( {name}, {surname}, {email}, {birthdate}, {country})"
    myCursor = None

    try:
        myCursor = connection.cursor()
        myCursor.execute(sqlQuery)
        print(myCursor.fetchone())
        myCursor.commit()
        myCursor.close()

    except Exception as error:
        infoLog.error(f"User {username} tried to create a new user but encountered an error: {error}")
        infoLog.debug(traceback.format_exc())
        print(traceback.format_exc())
        os.system("PAUSE")

    finally:
        if myCursor is not None:
            myCursor.close()

def obtainUsers():
    connection = connectDB
    if connectDB is None:
        return None
    users = None
    sqlQuery = "SELECT * FROM Usuarios"

    try:
        myCursor = connection.cursor()
        myCursor.execute(sqlQuery)
        users = myCursor.fetchall()
        myCursor.close()

    except Exception as error:
        print(f"SQL Query failed, error message: {error}")
        users = None
    finally:
        closeConn(connection)
    return users

def obtainUsersPurchases(userID):
    connection = connectDB
    if connectDB is None:
        return None
    purchases = None
    sqlQuery = f"SELECT * FROM Pedidos WHERE UserID = {userID}"

    try:
        myCursor = connection.cursor()
        myCursor.execute(sqlQuery)
        purchases = myCursor.fetchall()
    except Exception as error:
        print(f"SQL Query failed, error message: {error}")
        purchases = None
    finally:
        closeConn(connection)
    return purchases

def createUser(name, surname, email, birthDate, country):
    connection = connectDB
    if not connection:
        return False
    tableName = "Usuarios"
    sqlInsertionUser = f"INSERT INTO {tableName} (Nombre, Apellidos, Email, Fecha_de_nacimiento, Pais) VALUES "\
        f"('{name}','{surname}','{email}','{birthDate}','{country}')"
    myCursor = None
    try:
        myCursor = connection.cursor()
        myCursor.execute(sqlInsertionUser)
        print(myCursor.fetchone())
        myCursor.commit()
        myCursor.close()

    except Exception as error:
        infoLog.info(f"{error}")
    finally:
        if myCursor is not None:
            myCursor.close()

def modifyUserInfo(tableName, column, value, userID):
        
    tableName = "Usuarios"
    column = 'Fecha_de_nacimiento'
    value = '2000-09-19'

    connection = connectDB

    if not connection:
        return False

    sqlModifyBirthDate = f"UPDATE {tableName} SET {column} '{value}' WHERE UserId {userID}"

    myCursor = None
    try:
        myCursor = connection.cursor()
        myCursor.execute(sqlModifyBirthDate)
        print(myCursor.fetchone())
        myCursor.commit()
        myCursor.close()

    except Exception as error:
        infoLog.info(f"{error}")
    finally:
        if myCursor is not None:
            myCursor.close()

def delUser(tableName, userID):
        
    tableName = "Usuarios"

    connection = connectDB

    if not connection:
        return False

    sqlModifyBirthDate = f"DELETE FROM {tableName} WHERE UserId {userID}"

    myCursor = None
    try:
        myCursor = connection.cursor()
        myCursor.execute(sqlModifyBirthDate)
        print(myCursor.fetchone())
        myCursor.commit()
        myCursor.close()

    except Exception as error:
        infoLog.info(f"{error}")
    finally:
        if myCursor is not None:
            myCursor.close()

def createOrder(name, surname, email, birthDate, country, ):
    connection = connectDB

    if not connection:
        return False
    myCursor = None
    tableName = "Usuarios"
    tableOrder = "Pedidos"
    sqlInsertionUser = f"INSERT INTO {tableName} (Nombre, Apellidos, Email, Fecha_de_nacimiento, Pais) VALUES "\
            f"('{name}','{surname}','{email}','{birthDate}','{country}')"
    
    try:
        myCursor = connectDB.cursor()
        myCursor.execute(sqlInsertionUser)
        IDuser = myCursor.lastrowid #This is the id from the table Usuarios

        sqlInsertionOrder = f"INSERT INTO {tableOrder} (UserID, Fecha_de_pedido, Estado, Total) VALUES "\
            f"({IDuser}, '2024-04-22', 'en proceso', 0 )"

        myCursor.execute(sqlInsertionOrder)

        connection.commit()

    except Exception as error:
        connection.rollback()
        infoLog.info(f"{error}")
    finally:
        if myCursor is not None:
            myCursor.close()
        closeConn(connection)