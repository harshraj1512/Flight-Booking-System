import csv

class PersonRegistration():
    #constructor
    def __init__(self):
        self.personName = None
        self.noOfPerson = None
        self.departureLocation = None
        self.destinationLocation = None
        self.ddmmyyyy = None
        self.seatNo = None
        self.selectBusType = None
        self.busFare = None
        self.autoInc = 1
        self.countcol = 0

    def getPersonInfo(self):
        self.personName = input("Enter passenger Name : ")
        self.noOfPerson = int(input("Enter Number of passengers :"))
        print("1: chnadigardh")
        print("2: pune")
        print("3: Mumbai")
        print("4: Delhi")

        #Ente departure Locartion Name
        self.dl = int(input("Enter Departure Locartion"))
        if self.dl == 1:
            self.departureLocation = "chandigard"
        elif self.dl == 2:
            self.departureLocation = "pune"
        elif self.dl == 3:
            self.departureLocation = "Mumbai"
        elif self.dl == 4:
            self.departureLocation = "Delhi"
        else:
            print("please Enter correct Choice: ")

        #Arrival Location

        print("1: Gujrat")
        print("2: Banglore")
        print("3: Bhopal")
        print("4: Indore")

        self.dpl = int(input("Enter the Destination Location:"))
        if self.dpl == 1:
            self.destinationLocation = "Gujrat"
        elif self.dpl == 2:
            self.destinationLocation = "Banglore"
        elif self.dpl == 3:
            self.destinationLocation = "Bhopal"
        elif self.dpl == 4:
            self.destinationLocation = "Indore"

        #Date
        self.ddmmyyyy = input("Enter Date of Journey:")

        #Booking seat
        print("[1]__[2]__[3]__[4]__[5]__[6]__[7]__[8]__[9]__[10]")
        print("[11]__[12]__[13]__[14]__[15]__[16]__[17]__[18]__[19]__[20]")
        print("[21]__[22]__[23]__[24]__[25]__[26]__[27]__[28]__[29]__[30]")

        seatNoList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        self.bookingList=[]
        while True:
            self.seatNo = int(input("Choose a seat number: "))
            if self.seatNo <= 30:

                if self.seatNo in seatNoList:
                    self.bookingList.append(self.seatNo)
                    del seatNoList[self.seatNo+1]
                    count = len(seatNoList)
                else:
                    print("Ticket already Booked")
                print("Do you want to book one more seat Enter (Yes/No)")
                y = input("")
                if y == "yes":
                    pass
                else:
                    break

            else:
                print("seat No is not available")


        print("1: Ac Bus = $500")
        print("2: Non AC Bus = $300")
        self.busType = int(input("select bus Type:"))

        if self.busType == 1:
            self.selectBusType = "AC BUS"
            self.busFare = self.noOfPerson*500
        elif self.busType == 2:
            self.selectBusType = "NON AC BUS"
            self.busFare = self.noOfPerson*300


# saving passengerData
class passengerDataCsv(PersonRegistration):
    def saveInfo(self):
        try:
            with open("passengerData.csv",'r+',newline="") as f:
                r = csv.reader(f)
                data = list(r)
                #print(self.data)
                for i in data:
                    self.autoInc += 1
                    for j in i:
                        self.countcol += 1
                    print()
                print("Number of record in database:", self.autoInc)

        except:
            print("file has not available")
        finally:
            with open("passengerData.csv", 'a+', newline="") as f:
                w = csv.writer(f)
                w.writerow(([self.autoInc,self.personName,self.noOfPerson,self.departureLocation,self.destinationLocation,self.ddmmyyyy,self.bookingList,self.selectBusType,self.busFare]))
                print("Data save successfully")
                print()
