import datetime

class ATM(object):
    def __init__(self, cardNo, atmPIN, balance):
        self.cardNo = cardNo
        self.atmPIN = atmPIN
        self.balance = balance

    def displayBalance(self):
        return self.balance

    def addCash(self, cash):
        self.balance = self.balance + cash
        print(f"Cash Sucessfully Added. Your balance is Rs.{self.balance}")
        with open("MyDetails.txt", "a") as file:
            file.write(f"{datetime.datetime.now() } \t (Cr) Rs.{cash} \t Balance: {self.balance} \n")

    def cashWithdrawal(self,cash):
        if self.balance < cash :
            print("Cash unavaliable")
        else: 
            self.balance = self.balance - cash
            print(f"Rs.{cash} widthdrawl succesful. \n Available balance is Rs.{self.balance}")
            with open("MyDetails.txt", "a") as file:
                file.write(f"{datetime.datetime.now()} \t (Dr) Rs.{cash} \t Balance:{self.balance}       \n")


    def miniStatement(self):
        with open("MyDetails.txt", "r") as file:
            print(file.read())

    def changePIN(self, oldpin, newpin):
        if(self.atmPIN == oldpin):
            self.atmPIN = newpin
            print("ATM PIN changed succesfully!!!")
        else:
            print("Old Pin does not match. Sorry!!!")
            
cardNo = input("Enter Your 16 digit card no.: ")
atmPIN = input("Enter your 4 digit ATM PIN: ")
opt = 0

if(len(cardNo) != 16):
    print('Card number should be of 16 digits.')
    opt = 6
    
if(len(atmPIN) != 4):
    print('ATM PIN should be of 4 digits.')
    opt = 6

balance = 0

ATM1 = ATM(cardNo,atmPIN,balance)

with open("MyDetails.txt", "w") as file:
    file.write(f"Welcome Card No {cardNo} \n")

while opt!=6 : 
    print("What Operation You want to perform: ")
    print("1. Balance Enquiry")
    print("2. Add Cash")
    print("3. Widthdraw Cash")
    print("4. All Transactions")
    print("5. Change PIN")
    print("6. Exit (If you exit, your account will reset)")

    opt=int(input("Enter your option: "))

    if opt==1:
        print(f"Balance your account {ATM1.displayBalance()} \n")

    if opt==2 : 
        cash= int(input("Enter amount you want to add: "))
        ATM1.addCash(cash)

    if opt==3 : 
        cash= int(input("Enter amount you want to widthdraw: "))
        ATM1.cashWithdrawal(cash)

    if opt==4 : 
        ATM1.miniStatement()

    if opt==5 :
        oldpin = input("Enter your old ATM PIN: ")
        newpin = input("Enter your new ATM PIN: ")
        ATM1.changePIN(oldpin, newpin)