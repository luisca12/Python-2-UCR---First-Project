from sqlQueries import addUserDB, printUsers, showProducts, makePurchase, modifyStock, updateProductDetail, getAllPurchases, showPurchases, getSpecificPurchase
from connectHandler import connectDB, closeConn,hostname,username,dbName
from strings import greetingString,menuString,inputErrorString,newUserString
from log import logConfiguration
from functions import checkIsDigit, mkdir, checkYNInput

import os
import datetime
import logging.config
import traceback
import threading

def main():
    os.system("CLS")
    connection = connectDB()
    print(f"INFO: Connected to {hostname}, database: {dbName}")
    mkdir()
    logging.config.dictConfig(logConfiguration)
    infoLog = logging.getLogger('infoLog')
    while True:
        greetingString()
        menuString(hostname, username)
        selection = input("Please choose the option that yyou want: ")
        if checkIsDigit(selection):
            if int(selection) >= 5 or int(selection) == 0:
                print("Only numbers from 1 to 4 are accepted.")
                os.system("PAUSE")
            if selection == "1":
                userIDList,userNameList,userSurnameList = printUsers()
                while True:
                    currentUserID = input("\nPlease input your user ID (Numbers only): ")
                    if checkIsDigit(currentUserID):
                        if int(currentUserID) - 1 in range(len(userIDList)):
                            print(f"INFO: Customer selected: {userNameList[int(currentUserID) - 1]} {userSurnameList[int(currentUserID) - 1]}, user ID: {currentUserID}")
                            showPurchases(currentUserID, userNameList[int(currentUserID) - 1], userSurnameList[int(currentUserID) - 1])
                            while True:
                                currentOrderID = input("\n Please input your order ID (Numbers only):")
                                if checkIsDigit(currentOrderID):
                                    getAllPurchases(userNameList[int(currentUserID) - 1], userSurnameList[int(currentUserID) - 1], currentOrderID, currentUserID)
                                    break
                                else:
                                    inputErrorString()
                            break
                        else:
                            print(f"ERROR: User ID {currentUserID} does not exist in the database.")
                            os.system("PAUSE")
                    else:
                        inputErrorString()
                
                # Here continues option 1.
                getSpecificPurchase(currentOrderID, currentUserID,userNameList[int(currentUserID) - 1], userSurnameList[int(currentUserID) - 1])
                os.system("PAUSE")

            if selection == "2":
                userIDList,userNameList,userSurnameList = printUsers()
                while True:
                    userID = input("\nPlease select the user (user ID) that will make a purchase: ")
                    if checkIsDigit(userID):
                        if int(userID) - 1 in range(len(userIDList)):
                            print(f"INFO: User ID {userID} selected successfully.")
                            print(f"INFO: Making purchases for customer: {userNameList[int(userID) - 1]} {userSurnameList[int(userID) - 1]}, user ID: {userID}")
                            break
                        else:
                            print(f"ERROR: User ID {userID} does not exist in the database. Please choose between: {userIDList}")
                            os.system("PAUSE")
                    else:
                        inputErrorString()

                productIDList, productNameList, productPriceList, productStockList = showProducts()
                while True:
                    productID = input("\nPlease select the products (product ID) you want to buy (comma separated): ")
                    productIDs = productID.split(',')
                    
                    if all(checkIsDigit(pid.strip()) for pid in productIDs):
                        validPIDs = [int(pid.strip()) for pid in productIDs if int(pid.strip()) in productIDList]
                        invalidPIDs = [pid.strip() for pid in productIDs if int(pid.strip()) not in productIDList]

                        if validPIDs:
                            selectedProducts = []
                            selectedProductIDs = []
                            totalPrice = 0
                            for pid in validPIDs:
                                while True:
                                    quantity = input(f"How many devices of product {productNameList[productIDList.index(pid)]} with ID {pid} do you want? ")
                                    if checkIsDigit(quantity):
                                        quantity = int(quantity)
                                        if quantity > 0:
                                            break
                                        else:
                                            print(f"Quantity must be greater than 0. Please enter a valid quantity. Quantity chosen: {quantity}")
                                    else:
                                        inputErrorString()
                                selectedProducts.append((productNameList[productIDList.index(pid)], pid, quantity))
                                selectedProductIDs.append(pid)
                                totalPrice += productPriceList[productIDList.index(pid)] * quantity

                            print("INFO: Products selected successfully:")
                            for name, pid, quantity in selectedProducts:
                                print(f"\t{name} with ID {pid} - Quantity: {quantity}")
                                infoLog.info(f"Product selected successfully for user: {userNameList[int(userID) - 1]} " \
                                             f"{userSurnameList[int(userID) - 1]}, user ID: {userID}, product: {name} with ID {pid}, quantity {quantity}")
                            confirmation = input("Are you sure you want to continue?(y/n): ")
                            while not checkYNInput(confirmation):
                                print("Invalid input. Please enter 'y' or 'n'.\n")
                                infoLog.error(f"Syntax error. Expected input \"y\" or \"n\", actual input: {confirmation}")
                                confirmation = input("Are you sure you want to continue?(y/n): ")
                            if confirmation == "y":
                                currentDate = datetime.datetime.now().strftime("%Y-%m-%d")
                                orderID = makePurchase(userID, currentDate, totalPrice, {userNameList[int(userID) - 1]}, {userSurnameList[int(userID) - 1]})
                                for pid, quantity in zip(selectedProductIDs, [prod[2] for prod in selectedProducts]):
                                    newStock = productStockList[productIDList.index(pid)] - quantity
                                    modifyStock(pid, newStock, userID)
                                    updateProductDetail(orderID, userID, pid, quantity, productPriceList[productIDList.index(pid)], quantity * productPriceList[productIDList.index(pid)])
                                break
                        else:
                            print(f"ERROR: None of the provided product IDs {invalidPIDs} exist in the database. Please choose between: {productIDList}")
                            infoLog.error(f"None of the provided product IDs {invalidPIDs} by the user {userNameList[int(userID) - 1]} {userSurnameList[int(userID) - 1]}," \
                                          f"user ID: {userID} exist in the database. Current product list: {productIDList}")
                            os.system("PAUSE")
                    else:
                        print("ERROR: Invalid input format. Please enter a single number or a comma-separated list of numbers.")
                        infoLog.error(f"Syntax error when trying to choose the products. user {userNameList[int(userID) - 1]} {userSurnameList[int(userID) - 1]}," \
                                      f"tried to input: {productIDs}")
                        os.system("PAUSE")
                    
            if selection == "3":
                newUserString()
                name = input("Name: ")
                surname = input("Surname: ")
                email = input("Email: ")
                while True:
                    birthdate = input("Birthdate (format: YYYY-MM-DD): ")
                    try:
                        birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%d").date()
                        infoLog.info(f"Birthdate successfully added for user: {name}")
                        break
                    except Exception as error:
                        print("Invalid date format. Please enter the date in Year-Month-Day format.")
                        print(f"Error: {error}")
                        infoLog.error(f"Invalid date format. Date entered: {birthdate} by admin: {username}" \
                                    f" for new user: {name}, error: {error}")
                        infoLog.error(traceback.format_exc())
                country = input("Country: ")
                print("INFO: data succesfully saved")
                addUserDB(name, surname, email, birthdate, country)

            if selection == "4":
                closeConn(connection)
                infoLog.info(f"User {username} disconnected from the devices {hostname}")
                infoLog.info(f"User {username} logged out from the program.")
                break
        else:
            infoLog.error(f"Wrong option chosen in the menu: {selection}")
            inputErrorString()
            os.system("CLS")

if __name__ == "__main__":
    main()
