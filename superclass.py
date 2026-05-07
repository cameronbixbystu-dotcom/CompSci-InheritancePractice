class Automobile:
    def __init__(self, make, mileage, model, price):
        self.__make = make
        self.__mileage = mileage
        self.__model = model
        self.__price = price


    def set_make(self, make):
        self.__make = make


    def set_type(self, mileage):
        self.__mileage = mileage


    def set_age(self, model):
        self.__model = model

    def set_age(self, price):
        self.__price = price



    def get_make(self):
        return self.__make
   
    def get_type(self):
        return self.__mileage
   
    def get_age(self):
        return self.__model

    def get_age(self):
        return self.__price 


    def __str__(self):
        return f'make: {self.__make}\n' + \
            f'mileage: {self.__mileage}\n' + \
            f'model: {self.__model}\n' + \
            f'price: {self.__price}'
