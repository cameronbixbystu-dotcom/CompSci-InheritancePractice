import superclass


car_make = input("car make ")
car_mileage = input("car mileage ")
car_model = input("car model ")
car_price = input("car price ")
car_doors = input("car doors ")

entry = superclass.Car(car_make, car_mileage, car_model, car_price, car_doors)


truck_make = input("truck make ")
truck_mileage = input("truck mileage ")
truck_model = input("truck model ")
truck_price = input("truck price ")
truck_doors = input("truck doors ")

entry = superclass.Truck(truck_make, truck_mileage, truck_model, truck_price, truck_doors)




SUV_make = input("SUV make ")
SUV_mileage = input("SUV mileage ")
SUV_model = input("SUV model ")
SUV_price = input("SUV price ")
SUV_doors = input("SUV doors ")

entry = superclass.SUV(SUV_make, SUV_mileage, SUV_model, SUV_price, SUV_doors)