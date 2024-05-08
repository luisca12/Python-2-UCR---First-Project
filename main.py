import os
import sys
import pprint
from sqlQueries import addUserDB
from connectHandler import connectDB, closeConn,hostname,username
from strings import greetingString,menuString,inputErrorString,newUserString
from log import mkdir, infoLog
from functions import checkIsDigit
import logging

def main():
    os.system("CLS")
    mkdir()
    connection = connectDB()
    
    while True:
        greetingString()
        menuString(hostname, username)
        selection = input("Please choose the option that yyou want: ")
        if checkIsDigit(selection):
            if selection == "1":
                continue
            if selection == "3":
                newUserString()
                name = input("Name: ")
                surname = input("Surname: ")
                email = input("Email: ")
                birthdate = input("Birthdate: ")
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

if __name__ == "__main__":
    main()

# def main():
#     os.system("CLS")
#     mkdir()
    # users = obtainUsers()

    # for user in users:
    #     userID = user[0]
    #     name = f"{user[1]} {user[2]}"

    #     print(f"User purchases: {name}")
    #     purchases = obtainUsersPurchases(userID)
    #     for purchase in purchases:
    #         print(f"- #{purchase[0]} {purchase[3]}")
    #     print("-"*50)

# def main():
#     os.system("CLS")
#     connection = connectDB()
#     if not connection:
#         sys.exit("ERROR: Connection couldn't be established.")
#     myCursor = connection.cursor()
#     sqlQuery = "SELECT * FROM Productos"
#     sqlQuery1 = "SELECT Nombre, Precio FROM Productos"
#     sqlQuery2 = "SELECT Nombre, Precio FROM Productos WHERE Precio >= 300 AND Stock > 80"
#     try:
#         myCursor.execute(sqlQuery)
#         sqlQueryOut = myCursor.fetchall()
#         pprint.pprint(sqlQueryOut)
#     except Exception as error:
#         print(f"ERROR: couldn't run the query {sqlQuery}, error message: {error}")

