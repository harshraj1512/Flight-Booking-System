#Data Importing section
import csv

from personinfo import*

class Ticket:

    def ticket(self):
        bln = [] #list for storing data and retreving data from csv file
        with open("passengerData.csv", 'r+', newline="") as f:
            r = csv.reader(f)
            data = list(r)
            id = int(input("Enter your Booking id: "))
            for i in data:
                if id == int(i[0]):
                    for j in i:
                        bln.append(j)
                    break

        #print(bln)
        print("----------------------------------------")
        print("                     E Ticket            ")
        print("------------------------------------------")
        print()
        print(" E-Ticket:", "Bhopal Address          : Hingna Road T-Point")
        print("           ", "Phone no              : 4852552522255555")
        print()
        print("",bln[3],"--------->", bln[4],"        ","      passenger ID",bln[0])
        print()
        print("passenger Name: ",bln[1],"              ","Number of passenger: ",bln[2])
        print("-------------------------------------------------------------------------")
        print()
        print("Date of booking :",bln[5],"           ","seat no: ", bln[6],"             ")
        print()
        print("Bus Type:   ", bln[7],"                                         ")
        print("Bus Fare:   ", bln[8],"                                         ")
        print()
        print("----------------------------------------------------------------------------------")