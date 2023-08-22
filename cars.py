from enum import Enum
import os
import csv


class menu(Enum):
    ADD= 0
    DELETE= 1
    PRINT= 2
    SEARCH= 3
    EXIT= 4
    UPDATE= 5

cars=[]

def save_data(): 
    csv_file_path = "cars.csv"
    global cars 
# Open the CSV file in write mode
    with open(csv_file_path, mode="w", newline="") as csv_file:
    # Define the field names (header)
     fieldnames = ["color","model","type","id"]
    # Create a CSV writer object
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    # Write the header
    #csv_writer.writeheader()
    # Write the data
    for i in cars:
        csv_writer.writerow(i)

def clear_terminal():
    os_name = os.name

    if os_name == 'posix':  # For UNIX or Linux or MacOS
        os.system('clear')
    elif os_name == 'nt':  # For Windows
        os.system('cls')


def display_menu():
   for i in menu:
       print(f'{i.value} -  {i.name}')
   return menu(int(input("Enter a number")))

def cars_menu():
    while(True):
        user_res= display_menu()
        print(user_res)
        if user_res == menu.ADD: add_car()   
        if user_res == menu.DELETE: delete_car()
        if user_res == menu.PRINT:  print(cars)
        if user_res == menu.EXIT: return
        if user_res == menu.SEARCH: print(search_car())
        if user_res== menu.UPDATE: update_car()

def update_car():
    car_to_update= int(input("enter id"))
    key_change= input("enter color/model/company/id")
    # Find the dictionary for Bob and update it
    for i in cars:
        if car_to_update == i["id"] :
         i[key_change] = input("enter your update")
         break  # Once found and updated, break out of the loop

def delete_car():
    car_to_delete= search_car()
    cars.remove(car_to_delete)
    print(cars)

def search_car():
   car_to_find= input("enter car id")
   found_car= []
   for i in cars : 
        if car_to_find == i["id"]: 
         found_car = i 
   return found_car


def add_car():
    cars.append({
            "color": input("select color"),
            "model": input("select model"),
            "company": input("select company"),
            "id": int(input("enter id"))
        })
    

if __name__ == '__main__':
    # display_menu()
    clear_terminal()
    cars_menu()
    #save_data()



