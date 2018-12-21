#!/usr/bin/python
import mysql.connector

def connect():
    print('Connection successful')
    cnx = mysql.connector.connect(user='root', password='root',
    host = '127.0.0.1',
    database = 'phonebook')
    result = ''
    cursor = cnx.cursor()

    query = ("SELECT * FROM persons")

    cursor.execute(query)

    myresult = cursor.fetchall()

    for x in myresult:
        result = x
        print(x)

    cursor.close()
    cnx.close()
    return result
                                      
def print_menu():
    print('1. Print Phone Numbers')
    print('2. Add a Phone Number')
    print('3. Remove a Phone Number')
    print('4. Look up a Phone Number')
    print('5. Quit')
    print()

#Main menu, allows printing of existing numbers
#Also can add, remove and look up current phone numbers.

#INCLUDE AN INSERT FUNCTION TO PLACE NAMES AND NUMBERS INTO THE DATABASE.

numbers = {}
menu_choice = 0
#print_menu()
connect()

while menu_choice != 5:
    menu_choice = int(input("Type in a number (1-5): "))
    if menu_choice == 1:
        print("Telephone Numbers:")
        for x in numbers.keys():
            print("Name: ", x, "\tNumber:", numbers[x])
        print()
#Adding name (both first name and surname) and phone number
    elif menu_choice == 2:
        print("Add Name and Number")
        name = input("Name: ")
        phone = input("Number: ")
        numbers[name] = phone
#Deleting a name and number
    elif menu_choice == 3:
        print("Remove Name and Number")
        name = input("Name: ")
        if name in numbers:
            del numbers[name]
        else:
            print(name, "was not found")
#Looking up existing numbers using a person's name
    elif menu_choice == 4:
        print("Look up Number")
        name = input("Name: ")
        if name in numbers:
            print("The number is", numbers[name])
        else:
            print(name, "was not found")
#Closing the program
    elif menu_choice != 5:
        print_menu()
