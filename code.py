import superclass
import pickle




LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


FILENAME = 'cars.dat'


def main():
    myvehicles = load_pets()


    choice = 0


    while choice != QUIT:
        choice = get_menu_choice()


        if choice == LOOK_UP:
            look_up(myvehicles)
        elif choice == ADD:
            add(myvehicles)
        elif choice == CHANGE:
            change(myvehicles)
        elif choice == DELETE:
            delete(myvehicles)


    save_pets(myvehicles)






def load_pets():
    try:
        input_file = open(FILENAME, 'rb')


        pet_dct = pickle.load(input_file)


        input_file.close()
    except IOError:
        pet_dct = {}


    return pet_dct






def get_menu_choice():
    print()
    print("Menu")
    print("---------------------------")
    print('1. Look up a superclass')
    print('2. Add a new superclass')
    print('3. Change an existing superclass')
    print('4. Delete a superclass')
    print("5. Quite the program")
    print()


    choice = int(input('Enter a valid choice: '))


    return choice








def look_up(myvehicles):
    name = input("Enter a name: ")
    print(myvehicles.get(name, 'That name is not found.'))








def add(myvehicles):
    name = input('Name: ')
    type = input('type: ')
    age = input('age: ')


    entry = superclass.superclass(name, type, age)


    if name not in myvehicles:
        myvehicles[name] = entry
        print("The entry has been added.")
    else:
        print('That name already exists.')








def change(myvehicles):
    name = input('Enter a name: ')


    if name in myvehicles:
        type = input('Enter the new type: ')
        age = input('Enter the new age: ')
        entry = superclass.superclass(name, type, age)
        myvehicles[name] = entry
        print('Information updated.')
    else:
        print('That name is not found.')








def delete(myvehicles):
    name = input('Enter a name: ')
    if name in myvehicles:
        del myvehicles[name]
        print('Entry deleted.')
    else:
        print('That name is not found.')








def save_pets(myvehicles):
    output_file = open(FILENAME, 'wb')


    pickle.dump(myvehicles, output_file)


    output_file.close()


if __name__ == '__main__':
    main()

