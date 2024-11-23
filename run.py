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
        print("(4) View Wastage                                     ")
        print("(5) Exit.                                            ")
        print("=====================================================")

        choice = int(input("Enter your choice by entering number 1 to 5:"))
        print("\n")

        if choice == 1:
            viewInventory()
        elif choice == 2:
            addItemFromDelivery()
        elif choice == 3:
            removeItemFromUsage()
        elif choice == 4:
            viewWastage()
        elif choice == 5:
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
    """
    """
    while True:

        print("Please enter date and quantity of item recieve from delivery.")
        print("Data should begin with expiry date in the format of ddmmyyyy")
        print("and quantity to each hub B1, Y1, R1, B2, Y2, R2 separated by commas. ")
        print("Example: 21112024, 6, 6, 6, 6, 6, 6\n")

        delivery_input = input("Enter your data here: ")

        delivery_data = delivery_input.split(",")
        
        if validate_data(delivery_data):
            print("Data is valid!")
            break

        return delivery_data



def removeItemFromUsage():
    print("Please enter date and quantity of item that has been used")

def viewWastage():
    print("You are viewing the wastage data")
   
def validate_data(values):
    """
    """
    try:
        [int(value) for value in values]
        if len(values) != 7:
            raise ValueError(
                f"Exactly 7 values required with first being the expiry date (ddmmyyyy) then quantity for each hub"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True
                

get_user_choice()