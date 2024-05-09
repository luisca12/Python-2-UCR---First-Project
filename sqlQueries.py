from connectHandler import connectDB, closeConn,username,hostname,dbName
from log import logConfiguration

import traceback
import os
import datetime
import mysql.connector
import logging

infoLog = logging.getLogger('infoLog')

def addUserDB(name, surname, email, birthdate, country):
    # Step 1:
    connection = connectDB()
    if not connection:
        return False
    tableName = "Usuarios"
    sqlQuery = f"INSERT INTO {tableName} (Nombre, Apellido, Email, Fecha_de_nacimiento, Pais)" \
        f"VALUES ('{name}', '{surname}', '{email}', '{birthdate}', '{country}')"
    myCursor = None

    try:
        myCursor = connection.cursor()
        myCursor.execute(sqlQuery)
        connection.commit()
        print(f"INFO: User {name} added successfully to {tableName}!")
        infoLog.info(f"User added successfully to table:{tableName}. User data: name:{name}, surname:{surname}, " \
                     f"email:{email}, birthdate:{birthdate}, country:{country}")
        os.system("PAUSE")

    except Exception as error:
        infoLog.error(f"User {username} tried to create a new user but encountered an error: {error}")
        infoLog.debug(traceback.format_exc())
        print(traceback.format_exc())
        os.system("PAUSE")

    finally:
        if myCursor is not None:
            myCursor.close()
        closeConn(connection)

def printUsers():
    connection = connectDB()
    if not connection:
        return False
    tableName = "Usuarios"
    sqlQuery = f"SELECT * FROM {tableName}"
    myCursor = None
    try:
        myCursor = connection.cursor()
        myCursor.execute(sqlQuery)
        users = myCursor.fetchall()
        infoLog.info(f"Sucessfully obtained all the users inside the database {dbName}")
        print(f"\nUser ID\t", "Nombre".ljust(11),"Apellido".ljust(18),"Email".ljust(35),"Fecha De Nacimiento\t   Pais",)
        print("-"*109)
        userIDList = []
        userNameList = []
        userSurnameList = []
        for user in users:
            userIDList.append(user[0])
            userNameList.append(user[1])
            userSurnameList.append(user[2])
            userID, Nombre, Apellido, Email, Fecha_de_Nacimiento, Pais = user
            print(f"{userID}\t {Nombre.ljust(12)}{Apellido.ljust(19)}{Email.ljust(36)}{Fecha_de_Nacimiento}\t\t   {Pais}")
        print("-"*109)
        return userIDList,userNameList,userSurnameList
    
    except Exception as error:
        infoLog.error(f"There was an error printing all the users of the database, error: {error}")
        infoLog.debug(traceback.format_exc())
        print(traceback.format_exc())
        os.system("PAUSE")

    finally:
        if myCursor is not None:
            myCursor.close()
        closeConn(connection)



def showProducts():
    connection = connectDB()
    if not connection:
        return False
    tableName = "Productos"
    sqlQuery = f"SELECT * FROM {tableName}"
    myCursor = None
    try:
        myCursor = connection.cursor()
        myCursor.execute(sqlQuery)
        products = myCursor.fetchall()
        infoLog.info(f"Sucessfully obtained all the Products inside the database {dbName}")

        print(f"\nProductID\t", "Nombre".ljust(32),"Descripcion".ljust(80),"Precio\t","Stock",)
        print("-"*152)
        productIDList = []
        productNameList = []
        productPriceList = []
        productStockList = []
        for product in products:
            productIDList.append(product[0])
            productNameList.append(product[1])
            productPriceList.append(product[3])
            productStockList.append(product[4])
            ProductID, Nombre, Descripcion, Precio, Stock = product
            print(f"{ProductID}\t\t {Nombre.ljust(33)}{Descripcion.ljust(81)}{Precio}\t {Stock}")
        print("-"*152)
        return productIDList,productNameList,productPriceList,productStockList
    
    except Exception as error:
        infoLog.error(f"There was an error printing all the products of the database, error: {error}")
        infoLog.debug(traceback.format_exc())
        print(traceback.format_exc())
        os.system("PAUSE")

    finally:
        if myCursor is not None:
            myCursor.close()
        closeConn(connection)


def makePurchase(userID, currentDate, totalPrice, userName, userSurname):
    connection = connectDB()
    if not connection:
        return False
    tableName = "Pedidos"
    myCursor = None
    # Step 3: Make the purchase
    sqlQuery = f"INSERT INTO {tableName} (UserID, Fecha_de_pedido, Estado, Total) VALUES "\
         f"( {userID}, '{currentDate}', 'creado', {totalPrice} )"
    
    try:
        myCursor = connection.cursor()
        myCursor.execute(sqlQuery)
        connection.commit()
        orderID = myCursor.lastrowid
        print(f"INFO: Purchase successfully done for user: {userName} {userSurname}, {currentDate}, total price: {totalPrice}")
        os.system("PAUSE")
        infoLog.info(f"Purchase successfully done for user: {userID}, {currentDate}, total price: {totalPrice}")
        return orderID

    except Exception as error:
        infoLog.error(f"There was an error printing all the users in the database, error: {error}")
        infoLog.debug(traceback.format_exc())
        print(traceback.format_exc())
        os.system("PAUSE")

    finally:
        if myCursor is not None:
            myCursor.close()
        closeConn(connection)



def modifyStock(productID, newStock, userID):
    connection = connectDB()
    if not connection:
        return False
    tableName = "Productos"
    sqlQuery = f"UPDATE {tableName} SET Stock = {newStock} WHERE ProductID = {productID}"

    try:
        myCursor = connection.cursor()
        myCursor.execute(sqlQuery)
        connection.commit()
        infoLog.info(f"Product {productID} succesfully updated, new stock{newStock}. ")

    except Exception as error:
        infoLog.error(f"There was an error printing all the users in the database, error: {error}")
        infoLog.debug(traceback.format_exc())
        print(traceback.format_exc())
        os.system("PAUSE")

    finally:
        if myCursor is not None:
            myCursor.close()
        closeConn(connection)

def updateProductDetail(orderID, userID, productID, productAmount, unitPrice, subTotal):

    tableName2 = "Detalles_de_Pedido"
    sqlQuery = f"INSERT INTO {tableName2} (OrderID, ProductID, Cantidad, Precio_unitario, Subtotal)" \
         f"VALUES ({orderID}, {productID}, {productAmount}, {unitPrice}, {subTotal})"
    
    connection = connectDB()
    if not connection:
        return False

    try:
        myCursor = connection.cursor()
        myCursor.execute(sqlQuery)
        connection.commit()
        infoLog.info(f"Successfully updated {tableName2} with {orderID}, {productID}, {productAmount}, {unitPrice}, {subTotal}"\
                     f" for userID: {userID}")

    except Exception as error:
        infoLog.error(f"There was an error updating table: {tableName2}, error: {error}")
        infoLog.debug(traceback.format_exc())
        print(traceback.format_exc())
        os.system("PAUSE")

    finally:
        if myCursor is not None:
            myCursor.close()
        closeConn(connection)

def getAllPurchases(username, surname, orderID, userID):

    # Step 1: This is to obtain all the purchases registered
    tableName = "Pedidos"
    sqlQuery = f"SELECT * FROM {tableName}"
    
    # The above query will return something like this
    # [
    #     (1, 5, datetime.date, 'delivered', decimal.Decimal(1500)),
    #     (1, 5, datetime.date, 'delivered', decimal.Decimal(1500))
    # ]
    
    # Step 2: Obtain the details of a specific purchase
    tableName1 = "Detalles_de_Pedido"
    sqlQuery1 = f"SELECT * FROM {tableName1} WHERE OrderID = {orderID}"
    # The above query will return something like this
    # [
    #     (1, 5, 5, 10, 50),
    #     (1, 3, 5, 10, 50)
    # ]

    # Step 3: To obtain the informaion of a specific product 
    tableName2 = "Productos"
    sqlQuery2 = f"SELECT Nombre FROM {tableName2} WHERE ProductID = {orderID}"

    # Step 4: Bonus
    tableName3 = "Usuarios"
    sqlQuery3 = f"SELECT * FROM {tableName3} WHERE userID = {userID}"


    connection = connectDB()
    if not connection:
        return False

    try:
        myCursor = connection.cursor()

        myCursor.execute(sqlQuery)
        purchases = myCursor.fetchall()

        myCursor.execute(sqlQuery1)
        purchaseDetails = myCursor.fetchall()

        myCursor.execute(sqlQuery2)
        productNames = myCursor.fetchall()

        myCursor.execute(sqlQuery3)
        userDetails = myCursor.fetchall()

       
        # for purchase in purchases:
            

        # for detail in purchaseDetails:


        # for productName in productNames:


        # for userDetail in userDetails:

        
        # infoLog.info(f"Successfully obtained all the purchases for {username} {surname} with UserID: {userID}, OrderID: {orderID}")

    except Exception as error:
        infoLog.error(f"There was an error updating table: {tableName2}, error: {error}")
        infoLog.debug(traceback.format_exc())
        print(traceback.format_exc())
        os.system("PAUSE")

    finally:
        if myCursor is not None:
            myCursor.close()
        closeConn(connection)

def showPurchases(userID, name, surname):
    connection = connectDB()
    if not connection:
        return False
    tableName = "Pedidos"
    sqlQuery = f"SELECT * FROM {tableName} WHERE UserID={userID}"
    myCursor = None
    try:
        myCursor = connection.cursor()
        myCursor.execute(sqlQuery)
        orderIDs = myCursor.fetchall()
        infoLog.info(f"Sucessfully obtained all the Order IDs inside the database {dbName} for user ID {userID}")
        print(f"\nCurrent and old purchases for customer: {name} {surname}")
        print(f"\nOrderID\t", "UserID\t","Fecha de Pedido\t","Estado".ljust(20),"Total",)
        print("-"*71)

        for orderID in orderIDs:
            OrderID, UserID, Fecha_de_pedido, Estado, Total = orderID
            print(f"{OrderID}\t {UserID}\t {Fecha_de_pedido}\t\t {Estado.ljust(21)}{Total}")
        print("-"*71)
        return None
    
    except Exception as error:
        infoLog.error(f"There was an error printing all the users of the database, error: {error}")
        infoLog.debug(traceback.format_exc())
        print(traceback.format_exc())
        os.system("PAUSE")

    finally:
        if myCursor is not None:
            myCursor.close()
        closeConn(connection)

def getSpecificPurchase(orderID, userID, name, surname):
    tableName = "Detalles_de_Pedido"
    tableName1 = "Usuarios"
    sqlQuery = f"SELECT * FROM {tableName} WHERE OrderID={orderID}"
    sqlQuery1 = f"SELECT * FROM {tableName1} WHERE UserID={userID}"

    connection = connectDB()
    if not connection:
        return False

    try:
        myCursor = connection.cursor()
        myCursor1 = connection.cursor()

        myCursor.execute(sqlQuery)
        purchaseInfo = myCursor.fetchall()
        print(f"\nOrder ID: {orderID} for customer: {name} {surname}")
        print(f"\nOrderID\t", "Product ID\t","Cantidad\t", "Precio Unitario\t","Subtotal")
        print("-"*74)

        for purchaseInfoOut in purchaseInfo:
            OrderID, ProductID, Cantidad, Precio_unitario, Subtotal = purchaseInfoOut
            print(f"{OrderID}\t {ProductID}\t\t {Cantidad}\t\t {Precio_unitario}\t\t\t {Subtotal}")
        print("-"*74)
        infoLog.info(f"Successfully obtained specific informacion for Order ID: {orderID}")


        myCursor1.execute(sqlQuery1)
        userInfo = myCursor1.fetchall()
        print(f"\nSpecific Customer Information: {name} {surname}")
        print(f"\nUser ID\t", "Nombre".ljust(11),"Apellido".ljust(18),"Email".ljust(35),"Fecha De Nacimiento\t   Pais",)
        print("-"*109)

        for userInfoOut in userInfo:
            UserID, Nombre, Apellido, Email, Fecha_de_Nacimiento, Pais = userInfoOut
            print(f"{UserID}\t {Nombre.ljust(12)}{Apellido.ljust(19)}{Email.ljust(36)}{Fecha_de_Nacimiento}\t\t   {Pais}")
        print("-"*109)
        infoLog.info(f"Successfully obtained specific informacion for user: {name} {surname}, user ID: {userID}")        

    except Exception as error:
        infoLog.error(f"There was an error getting the specific Order ID: {orderID}, error: {error}")
        infoLog.debug(traceback.format_exc())
        print(traceback.format_exc())
        os.system("PAUSE")

    finally:
        if myCursor is not None:
            myCursor.close()
        if myCursor1 is not None:
            myCursor1.close()
    closeConn(connection)

# def obtainUsers():
#     connection = connectDB
#     if connectDB is None:
#         return None
#     users = None
#     sqlQuery = "SELECT * FROM Usuarios"

#     try:
#         myCursor = connection.cursor()
#         myCursor.execute(sqlQuery)
#         users = myCursor.fetchall()
#         myCursor.close()

#     except Exception as error:
#         print(f"SQL Query failed, error message: {error}")
#         users = None
#     finally:
#         closeConn(connection)
#     return users

# def obtainUsersPurchases(userID):
#     connection = connectDB
#     if connectDB is None:
#         return None
#     purchases = None
#     sqlQuery = f"SELECT * FROM Pedidos WHERE UserID = {userID}"

#     try:
#         myCursor = connection.cursor()
#         myCursor.execute(sqlQuery)
#         purchases = myCursor.fetchall()
#     except Exception as error:
#         print(f"SQL Query failed, error message: {error}")
#         purchases = None
#     finally:
#         closeConn(connection)
#     return purchases

# def createUser(name, surname, email, birthDate, country):
#     connection = connectDB
#     if not connection:
#         return False
#     tableName = "Usuarios"
#     sqlInsertionUser = f"INSERT INTO {tableName} (Nombre, Apellidos, Email, Fecha_de_nacimiento, Pais) VALUES "\
#         f"('{name}','{surname}','{email}','{birthDate}','{country}')"
#     myCursor = None
#     try:
#         myCursor = connection.cursor()
#         myCursor.execute(sqlInsertionUser)
#         print(myCursor.fetchone())
#         myCursor.commit()
#         myCursor.close()

#     except Exception as error:
#         infoLog.info(f"{error}")
#     finally:
#         if myCursor is not None:
#             myCursor.close()

# def modifyUserInfo(tableName, column, value, userID):
        
#     tableName = "Usuarios"
#     column = 'Fecha_de_nacimiento'
#     value = '2000-09-19'

#     connection = connectDB

#     if not connection:
#         return False

#     sqlModifyBirthDate = f"UPDATE {tableName} SET {column} '{value}' WHERE UserId {userID}"

#     myCursor = None
#     try:
#         myCursor = connection.cursor()
#         myCursor.execute(sqlModifyBirthDate)
#         print(myCursor.fetchone())
#         myCursor.commit()
#         myCursor.close()

#     except Exception as error:
#         infoLog.info(f"{error}")
#     finally:
#         if myCursor is not None:
#             myCursor.close()

# def delUser(tableName, userID):
        
#     tableName = "Usuarios"

#     connection = connectDB

#     if not connection:
#         return False

#     sqlModifyBirthDate = f"DELETE FROM {tableName} WHERE UserId {userID}"

#     myCursor = None
#     try:
#         myCursor = connection.cursor()
#         myCursor.execute(sqlModifyBirthDate)
#         print(myCursor.fetchone())
#         myCursor.commit()
#         myCursor.close()

#     except Exception as error:
#         infoLog.info(f"{error}")
#     finally:
#         if myCursor is not None:
#             myCursor.close()

# def createOrder(name, surname, email, birthDate, country, ):
    # connection = connectDB

    # if not connection:
    #     return False
    # myCursor = None
    # tableName = "Usuarios"
    # tableOrder = "Pedidos"
    # sqlInsertionUser = f"INSERT INTO {tableName} (Nombre, Apellidos, Email, Fecha_de_nacimiento, Pais) VALUES "\
    #         f"('{name}','{surname}','{email}','{birthDate}','{country}')"
    
    # try:
    #     myCursor = connectDB.cursor()
    #     myCursor.execute(sqlInsertionUser)
    #     IDuser = myCursor.lastrowid #This is the id from the table Usuarios

    #     sqlInsertionOrder = f"INSERT INTO {tableOrder} (UserID, Fecha_de_pedido, Estado, Total) VALUES "\
    #         f"({IDuser}, '2024-04-22', 'en proceso', 0 )"

    #     myCursor.execute(sqlInsertionOrder)

    #     connection.commit()

    # except Exception as error:
    #     connection.rollback()
    #     infoLog.info(f"{error}")
    # finally:
    #     if myCursor is not None:
    #         myCursor.close()
    #     closeConn(connection)