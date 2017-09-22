# Airline Booking Reservation System
#flight,person,employee,passenger

class person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    def display(self):
        print("My name is %s and I'm %d"%(self.name,self.__age))


class account:
    def __init__(self,name,amount):
        self.name = name
        self.__amount = amount
    #passenger pay for the reservation. if there's enough money, it will be paid successfully, otherwise it will fail
    def pay(self,price):
        if self.__amount >= price:
            self.__amount -= price
            return True
        else:
            return False
    def display(self):
        print("There are $%f left in my account"%self.__amount)


class flight():
    def __init__(self,flightnumber,seatnum,price):
        self.flightnumber = flightnumber
        self.seatnum = seatnum
        self.price = price
    def display(self):
        print("the airline number is %s and there are %d seats remain."%(self.flightnumber,self.seatnum))
        print("The price for this flight is %f"%self.price)


class employee(person):
    def __init__(self,name,age,flight):
        person.__init__(self,name,age)
        self.flight = flight
    def display(self):
        person.display(self)
        print("I work for %s"%self.flight.flightnumber)


class passenger(person,account):
    def __init__(self,name,age,amount):
        person.__init__(self,name,age)
        account.__init__(self,name,amount)
    # passenger will reserve successfully only if there are available seats and paid successfully
    def reserve(self,flight):
        if flight.seatnum != 0:
            if(self.pay(flight.price)):
                flight.seatnum -=1
                print("reserve successfully")
            else:
                print("fail to pay for the reservation")
        else:
            print("There's no seat, fail to reserve")
    def display(self):
        person.display(self)
        account.display(self)


AA183 = flight("AA183",50,100)
AA154 = flight("AA154",0,70)
Anna = employee("Anna",27,AA183)
Ben = passenger("Ben",18,1000)
John = passenger("John",23,80)

Anna.display()
Ben.display()
John.display()
AA183.display()
AA154.display()

Ben.reserve(AA183)
AA183.display()
Ben.display()

John.reserve(AA183)
John.reserve(AA154)