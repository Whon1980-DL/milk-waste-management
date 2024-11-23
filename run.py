import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('milk_waste_management')

def get_user_choice():
    """
    Get user to select choice
    """

    while True:

        print("=====================================================")
        print("= Welcome to DISC Milk Waste Management Application =")
        print("=====================================================")
        print("(1) View Inventory                                   ")
        print("(2) Receive Delivery                                 ")
        print("(3) Record Usage                                     ")
        print("(4) Record Wastage                                   ")
        print("(5) Record Redistribution                            ")
        print("(6) Exit.                                            ")
        print("=====================================================")

        choice = int(input("Enter your choice by entering number 1 to 6:"))
        print("\n")

        if choice == 1:
            viewInventory()
        elif choice == 2:
            addItemFromDelivery()
        elif choice == 3:
            removeItemFromUsage()
        elif choice == 4:
            removeItemFromWastage()
        elif choice == 5:
            redistribution()
        elif choice == 6:
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

def viewInventory():
    """
    """
    inventory = SHEET.worksheet('inventory')
    inventory_data = inventory.get_all_values()

    for inventory_data in inventory_data:
        print(inventory_data)
    
    print("\n")

def addItemFromDelivery():
    print("Please enter date and quantity of item recieve from delivery")
    print("Data should begin with expiry date in the order of dd-mmm-yyy")
    print("follow by =Today() and quantity to each hub ")
    print("B1, Y1, R1, B2, Y2, R2 separated by commas.")
    print("Example: 30-Nov-2024, =TODAY(), 6, 6, 6, 6, 6, 6\n")

    delivery_input = input("Enter your data here: ")

    delivery_data = delivery_input.split(",")
    print(delivery_data)

def removeItemFromUsage():
    print("Please enter date and quantity of item that has been used")
   


get_user_choice()