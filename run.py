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
            removeItemByUsage()
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
    inventory_worksheet = SHEET.worksheet('inventory')
    inventory_data = inventory_worksheet.get_all_values()

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
    
    update_delivery_worksheet(delivery_data)
    update_inventory_worksheet(delivery_data)

    return delivery_data

def update_delivery_worksheet(data):
    """
    """
    print("Updating delivery worksheet...\n")
    delivery_worksheet = SHEET.worksheet('delivery')
    delivery_worksheet.append_row(data)
    print("Delivery worksheet updated successfully.\n")

def update_inventory_worksheet(data):
    """
    """
    print("Updating inventory worksheet...\n")
    inventory_worksheet = SHEET.worksheet('inventory')
    inventory_worksheet.append_row(data)
    print("Inventory worksheet updated successfully with deleivery data.\n")

def removeItemByUsage():
    """
    """

    expiryDateOfMilkUsed()
    areaOfMilkUsed()

def expiryDateOfMilkUsed():
    while True:
        print("Please enter expiry date of milk to be used (ddmmyyyy)")

        date_input = input("Please enter expiry date here: ")

        if validate_date_input(date_input):
            print(f"The date you entered is {date_input}\n")
            print("Date is valid!\n")
            break

    return date_input

def areaOfMilkUsed():
    while True:
        print("Please enter the location for the milk to be used")

        area_used = input("Please enter area here: ")

        if validate_area_input(area_used):
            print(f"The area entered is {area_used}\n")
            print("Area is valid!")
            break

    return area_used
    
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

def validate_date_input(values):
    """
    """
    try:
        [int(value) for value in values]
        if len(values) != 8:
            raise ValueError(
                f"Exactly 8 digits number required in this format ddmmyyyy, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

def validate_area_input(value):
    """
    """
    try:
        if value not in {"B1", "Y1", "R1", "B2", "Y2", "R2"}:
            raise ValueError(
                f"Value has to be B1 or Y1 or R1 or B2 or Y2 or R2"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True   

                

get_user_choice()