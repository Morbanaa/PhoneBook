"""
Phone Book Program
Morbanaa Studios
Created by: Teddy Rodd

Requirements: 
Install the mysql-connector-python package before running main.py
"""
import mysql.connector
import os
import platform


#================================
#       Main Loop
#================================
def main():
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="mydb"
    )

    in_book = False
    
    # Get User Choice
    while True:
        clear_screen()
        print("Would You Like To:\n(1) Add a phone number:\n(2) Remove a phone number:\n(3) Print phone book:\n(4) Exit Program")
        choice = input("Choose: ")

        # Activate Function
        match choice:
            case "1": 
                in_book = False
                add_row(conn,in_book)
            case "2": 
                in_book = False
                remove_row(conn,in_book)
            case "3": 
                in_book = True
                printDB(conn,in_book)
            case "4":
                break
            case _: 
                clear_screen() # Clear screen and loop back
                continue

    conn.close()


#================================
#       Add Phone Number
#================================
def add_row(conn,in_book):
    # Collects Values Sends to MySQL
    clear_screen()
    while True:
        cursor = conn.cursor() # Oppen Conection

        printDB(conn,in_book)
        phone_book = []
        choice = input("\nEnter their name: ").upper()
        if choice == "Q": # Return To Menu
            break
        phone_book.append(choice)
       
        choice = input("Enter their phone number: ").upper()
        if choice == "Q": # Return To Menu
            break
        phone_book.append(choice)
        
        query = "insert into phone_book (name,phone) values (%s,%s)"
        cursor.execute(query,phone_book)
        conn.commit()
        phone_book.clear()

        cursor.close() # Close Conection


#================================
#       Remove Row
#================================
def remove_row(conn,in_book):
    clear_screen()

    while True:
        cursor = conn.cursor() # Open Conection

        printDB(conn,in_book)

        selection = []
        choice = input("\nEnter the ID of who you would like to remove from the phone book: ").upper()
        selection.append(choice)

        if choice == "Q": # Return To Menu
            break

        query = "delete from phone_book where ID = (%s)"
        cursor.execute(query,selection)
        conn.commit()
        selection.clear()

        cursor.close() # Close Conection


#================================
#       Print Database
#================================
def printDB(conn,in_book):

    cursor = conn.cursor() # Opens Conection

    # Pulls Values From MySQL In Order A - Z
    cursor.execute("SELECT * FROM phone_book ORDER BY name ASC")
    results = cursor.fetchall()

    clear_screen()
    if in_book == False:
        print("Enter (Q) to Quit At Any Time...\n")
    # Prints Values
    print(f"ID: --------------------- Name: --------------------- Phone Number:")
    print("------------------------------------------------------------------- \n")
    for row in results:
        for value in row:
            print(f"{value:<27}",end="")
        print()
    print("------------------------------------------------------------------- \n")
    cursor.close() # Close Conection

    if in_book == True:
        input("\nEnter any key to return to menu...\n")


#================================
#       Wipe Screen
#================================
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

        # SELECT * FROM table_name ORDER BY column_name ASC;


#================================
#       Program Entry Point
#================================
if __name__ == "__main__":
    main()

    # Last Message
    clear_screen()
    print("Don't Have Good Day, Have A Great Day : )\n")
