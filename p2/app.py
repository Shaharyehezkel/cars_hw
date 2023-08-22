from enum import Enum
import os
import json

class Actions(Enum):
    PRINT = 0
    ADD =1
    DELETE =2
    SEARCH =3
    EXIT =5
    SAVE =7

contacts =[]

def save_2_file():
    with open("contacts.json", "w") as f:
        json.dump(contacts, f)

def display_menu():
    for x in Actions: print(f'{x.value}  - {x.name}' )
    return Actions(int(input("your selection")))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while(True):
        user_selection =display_menu()
        if user_selection == Actions.PRINT : print( contacts)
        if user_selection == Actions.ADD : contacts.append({"name":input("please enter your name"),"tel":input("enter your tel num")})
        if user_selection == Actions.DELETE: 
            del_contact()
        if user_selection == Actions.SEARCH : find_contact()
        if user_selection == Actions.EXIT: return
        print(f"your selection is: {Actions( user_selection).name}")

def del_contact():
    contact =find_contact()
    if contact != None:
        contacts.remove(contact)
        print("del" , contact)
    else:
        print("no such contact")

def find_contact():
    found=False
    found_contact=""
    search =input("give me name 2 search")
    for contact in contacts:
        if contact["name"]==search:
            found =True
            found_contact =contact
    if found :
        print(found_contact)
        return found_contact
    return None

if __name__ == '__main__':
    clear_screen()
    menu()
    save_2_file()
    print("Thank u 4 using my program")