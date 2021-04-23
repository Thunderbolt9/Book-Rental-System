class BookRentShop:
    def __init__(self):
        self.name = ""
        self.mobile_number = 0
        self.email = ""
        self.bookList = {"In Search of Lost Time": 10,
                    "Ulysses": 10,                                        
                    "Don Quixote": 10,
                    "The Great Gatsby": 10,
                    "War and Peace": 5,
                    "The Odyssey": 5,
                    "Hamlet": 7,
                    "The Divine Comedy": 5,
                    "Alice's Adventures in Wonderland": 7,
                    "Gullivers Travels": 3}

        self.namebook = ""
        self.quantbook = 0
        self.amount = 0
        self.duration = ""
        self.flag = 0


# =================== Method to get information of the books in shop =========================
    def inventory(self):
        for book in self.bookList:
            print(book, ",", self.bookList[book])

# =================== Method to get information of availabilty of books ========================
    def bookrent(self, bookname, quantity):
        if((bookname in self.bookList) and (quantity <= self.bookList[bookname])):
            self.namebook = bookname
            self.quantbook = quantity
            self.flag = 1
            return True
        else:
            return False

# =================== Method to calculate Price of Book ========================
    def pricebook(self, duration, promocode):
        self.duration = duration
        l = duration.split(',')
        number = int(l[0])
        code = "super30"
        if(promocode==code):
            if(l[1]=="hours"):
                price = (12*number) - ((12*number)*0.3)

            elif(l[1]=="days"):
                price = (15*number) - ((15*number)*0.3)

            else:
                price = (30*number) - ((30*number)*0.3)

        else:
            if(l[1]=="hours"):
                price = (12*number)

            elif(l[1]=="days"):
                price = (15*number)

            else:
                price = (30*number)

        self.amount = price*self.quantbook

        
# =================== Method to generate bill ========================
    def bill(self,name, mobile_number, email):
        self.name = name
        self.mobile_number = mobile_number
        self.email = email
        if(self.flag==1):
            print("                    Book center")
            print("--------------------------------------------------------------")
            print("Name: {}".format(self.name))
            print("Mobile: {}".format(self.mobile_number))
            print("Email: {}".format(self.email))
            print("---------------------------------------------------------------")
            print("Book: {}".format(self.namebook))
            print("Quantity: {}".format(self.quantbook))
            print("Duration: {}".format(self.duration))
            print("Amount: {} ruppees".format(self.amount))
            self.bookList[self.namebook] = self.bookList[self.namebook]- self.quantbook
            



print("                    Welcome to Book center")
print("==============================================================")
print("To check books in inventory write command: <types_of_books>")
print("To buy particular book write command: <want_book>")
print("==============================================================")
print()

c1 = BookRentShop()

while(True):
    cust_request = input("How can we help you: ")
    if(cust_request == "<types_of_books>"):
        c1.inventory()
        for _ in range(0,5):
            print()
        
    elif(cust_request == "<want_book>"):
        bookname = input("Which book you want: ")
        quantity = int(input("How much such books you require: "))
        if((c1.bookrent(bookname, quantity))== True):
            print("Yes, we have your requirements")
            print()
        
            duration = input("How long do you require the book for: ")
            promocode = input("Do you have any promotion code with you: ")
            c1.pricebook(duration, promocode)
            print()

            print("For the bill")

            name = input("Tell me your name: ")
            mobile = input("Tell me your mobile: ")
            email = input("Tell me your email: ")

            print()
            print("Here is your bill")
            print()
            print("-------------------------------------------------------------")
            c1.bill(name, mobile, email)
        else:
            print()
            print("We are less in stock, Sorry for inconvenience!!!")

    else:
        break
