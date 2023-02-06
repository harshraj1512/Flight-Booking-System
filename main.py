import mysql.connector

# servername = '127.0.0.1:3307'
servername = 'localhost'

username = 'root'
password = ''
database = 'mysql'



cnx = mysql.connector.connect(servername,username, password,database)






# Data Importing
from personinfo import*
from Ticket import*
from admin import*

global ch

print("----------------------------")
print("        E-Ticket            ")
print("----------------------------")
print()

def start():
    print("1: Admin Registration: ")
    print("2: Admin Login: ")
    print()
    adminObj = Admin()
    ch = int(input("Choose:"))

    if ch == 1:
        adminObj.adminRegistration()

    if ch == 2:
        adminObj.adminLogin()

    print()
    print("1: Passenger Registartion: ")
    print("2: Ticket : ")
    print()
    ch = int(input("Choose: "))
    if ch == 1:
        pd_obj = passengerDataCsv()
        pd_obj.getPersonInfo()
        pd_obj.saveInfo()
    elif ch == 2:
        obj = Ticket()
        obj.ticket()

start()