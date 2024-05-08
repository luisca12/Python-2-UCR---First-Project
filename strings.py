import os

def greetingString():
    os.system("CLS")
    print('  ------------------------------------------------- ')
    print("           Welcome to the database program ")
    print('  ------------------------------------------------- ')

def menuString(deviceIP, username):
    os.system("CLS")
    print(f"Connected to: {deviceIP} as {username}\n")
    print('  -------------------------------------------------------------- ')
    print('\t\tMenu - Please choose an option')
    print('\t\t  Only numbers are accepted')
    print('  -------------------------------------------------------------- ')
    print('  >\t\t1. Consultar Pedidos\t\t\t       <')
    print('  >\t\t2. Realizar Pedido\t\t\t       <')
    print('  >\t\t3. Registrarse\t\t\t\t       <')
    print('  >\t\t4. Salir\t\t\t\t       <')
    print('  -------------------------------------------------------------- \n')

def inputErrorString():
    os.system("CLS")
    print('  ------------------------------------------------- ')  
    print('>      INPUT ERROR: Only numbers are allowed       <')
    print('  ------------------------------------------------- ')
    os.system("PAUSE")

def newUserString():
    os.system("CLS")
    print('  ------------------------------------------------- ')
    print("           You have chosen to input a new user ")
    print("          Please fill the following information")
    print('  ------------------------------------------------- ')