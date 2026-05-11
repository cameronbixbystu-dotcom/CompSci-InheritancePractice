import superclass
import pickle





FILENAME = 'cars.dat'

def load_cars():
    try:
        input_file = open(FILENAME, 'rb')


        car_dct = pickle.load(input_file)


        input_file.close()
    except IOError:
        car_dct = {}


    return car_dct


mycars = load_cars()





car_make = input("car make: ")
car_mileage = input("car mileage: ")
car_model = input("car model: ")
car_price = input("car price: ")
car_doors = input("car doors: ")

entry1 = superclass.Car(car_make, car_mileage, car_model, car_price, car_doors)
mycars[car_make] = entry1


truck_make = input("truck make: ")
truck_mileage = input("truck mileage: ")
truck_model = input("truck model: ")
truck_price = input("truck price: ")
truck_doors = input("truck doors: ")

entry2 = superclass.Truck(truck_make, truck_mileage, truck_model, truck_price, truck_doors)
mycars[truck_make] = entry2



SUV_make = input("SUV make: ")
SUV_mileage = input("SUV mileage: ")
SUV_model = input("SUV model: ")
SUV_price = input("SUV price: ")
SUV_doors = input("SUV doors: ")

entry3 = superclass.SUV(SUV_make, SUV_mileage, SUV_model, SUV_price, SUV_doors)
mycars[SUV_make] = entry3


name = input("Enter a car make: ")
print(mycars.get(car_make, 'That name is not found.'))


name = input("Enter a truck make: ")
print(mycars.get(truck_make, 'That name is not found.'))


name = input("Enter a SUV make: ")
print(mycars.get(SUV_make, 'That name is not found.'))