class Automobile:
    def __init__(self, make, mileage, model, price):
        self.__make = make
        self.__mileage = mileage
        self.__model = model
        self.__price = price


    def set_make(self, make):
        self.__make = make


    def set_mileage(self, mileage):
        self.__mileage = mileage


    def set_model(self, model):
        self.__model = model

    def set_price(self, price):
        self.__price = price



    def get_make(self):
        return self.__make
   
    def get_mileage(self):
        return self.__mileage
   
    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price 


    def __str__(self):
        return f'make: {self.__make}\n' + \
            f'mileage: {self.__mileage}\n' + \
            f'model: {self.__model}\n' + \
            f'price: {self.__price}'

class Car(Automobile):
    def __init__(self, make, model, mileage, price, doors):
        super().__init__(make, model, mileage, price)
        self.doors = doors
    
    def set_doors(self, doors):
        self.__doors = doors

    def get_doors(self):
        return self.__doors
    


class Truck(Automobile):
    def __init__(self, make, model, mileage, price, drive):
        super().__init__(make, model, mileage, price)
        self.drive = drive
    
    def set_drive(self, drive):
        self.__drive = drive

    def get_drive(self):
        return self.__drive
    


class SUV(Automobile):
    def __init__(self, make, model, mileage, price, seats):
        super().__init__(make, model, mileage, price)
        self.seats = seats
    
    def set_seats(self, seats):
        self.__seats = seats

    def get_seats(self):
        return self.__seats
    
