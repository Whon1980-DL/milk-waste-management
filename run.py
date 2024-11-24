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
            view_inventory()
        elif choice == 2:
            add_item_from_delivery()
        elif choice == 3:
            remove_item_by_usage()
        elif choice == 4:
            view_wastage()
        elif choice == 5:
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

def view_inventory():
    """
    """
    inventory_worksheet = SHEET.worksheet('inventory')
    inventory_data = inventory_worksheet.get_all_values()

    for inventory_data in inventory_data:
        print(inventory_data)
    
    print("\n")

def add_item_from_delivery():
    """
    """
    while True:

        print("Please enter date and quantity of item recieve from delivery.")
        print("Data should begin with expiry date in the format of ddmmyyyy and quantity")
        print("to each hub B1, Y1, R1, B2, Y2, R2 respectively separated by commas.")
        print("Example: 21112024, 6, 6, 6, 6, 6, 6\n")

        delivery_input = input("Enter your data here: ")

        delivery_data = delivery_input.split(",")
        
        if validate_delivery_data(delivery_data):
            print("Data is valid!")
            break

    update_delivery_worksheet(delivery_data)
    update_inventory_worksheet(delivery_data)
    add_data_to_remove_by_using_and_wasting_worksheet(delivery_data)

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

def add_data_to_remove_by_using_and_wasting_worksheet(data):
    """
    """
    """while True:
        print("Please enter the expiry date of the milk in the delivery (ddmmyyyy) followed by 0,0,0,0,0,0")
        print("to update remove_by_using and remove_by_wasting worksheet")
        print("Example: 21112024, 0, 0, 0, 0, 0, 0\n")

        expiry_date_input = input("Enter your data here: ")

        expiry_date_input_data = expiry_date_input.split(",")
        
        if validate_data(expiry_date_input_data):
            print("Data is valid!")
            break
    
    return expiry_date_input_data"""

    new_expiry_date = data[0]
    new_expiry_date_to_update_usage_wastage = [new_expiry_date, '0', '0', '0', '0', '0', '0']
    
    return new_expiry_date_to_update_usage_wastage

"""def update_remove_by_using_worksheet_with_new_expiry_date(data):"""

def remove_item_by_usage():
    """
    """

    date_input_value = expiry_date_of_milk_used()

    area_used_value = area_of_milk_used()

    number_bottle_used_value = quantity_of_milk_used()

    usage_worksheet = SHEET.worksheet('remove_by_using')
    coordinate1 = usage_worksheet.find(date_input_value)
    row = coordinate1.row
    coordinate2 = usage_worksheet.find(area_used_value)
    column = coordinate2.col

    cell_value = int(usage_worksheet.cell(row, column).value)

    new_cell_value = cell_value + number_bottle_used_value

    usage_worksheet.update_cell(row, column, new_cell_value)

    print("Remove_by_using wroksheet updated successfully....\n")

def expiry_date_of_milk_used():
    while True:
        print("Please enter expiry date of milk to be used (ddmmyyyy)")

        date_input = input("Please enter expiry date here: ")

        if validate_date_input(date_input):
            print(f"The date you entered is {date_input}\n")
            print("Date is valid!\n")
            break

    return date_input

def area_of_milk_used():
    while True:
        print("Please enter the location for the milk to be used")

        area_used = input("Please enter area here: ")

        if validate_area_input(area_used):
            print(f"The area entered is {area_used}\n")
            print("Area is valid!\n")
            break

    return area_used

def quantity_of_milk_used():
    while True:
        print("Please enter the number of bottle of milk used")

        number_of_bottle_used = int(input("Please enter the number of bottle here: "))

        if validate_number_of_bottle_input(number_of_bottle_used):
            print(f"The number of bottle entered is {number_of_bottle_used}\n")
            print("The number is valid!\n")
            break

    return number_of_bottle_used
    
def view_wastage():
    print("You are viewing the wastage data")
   
def validate_delivery_data(values):
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

def validate_number_of_bottle_input(value):
    """
    """
    try:
        if value == 0:
            raise ValueError(
                f"Number of bottle entered must not be 0"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True   


                

get_user_choice()
