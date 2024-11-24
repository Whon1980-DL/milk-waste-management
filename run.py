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
        print("(4) Record Wastage                                     ")
        print("(5) Exit.                                            ")
        print("=====================================================")

        choice = int(input("Enter your choice by entering number 1 to 5:\n"))
        print("\n")

        if choice == 1:
            view_inventory()
        elif choice == 2:
            add_item_from_delivery()
        elif choice == 3:
            remove_item_by_usage()
        elif choice == 4:
            remove_item_by_wastage()
        elif choice == 5:
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

def view_inventory():
    """
    Display inventory to user, using for loop to make data displayed more user friendly
    """
    inventory_worksheet = SHEET.worksheet('inventory')
    inventory_data = inventory_worksheet.get_all_values()

    for inventory_data in inventory_data:
        print(inventory_data)
    
    print("\n")

def add_item_from_delivery():
    """
    Collect delivery data from user to update delivery and inventory worksheet
    and run a funciton to get expiry date to use with usage and wastage worksheet
    """
    while True:

        print("Please enter date and quantity of item recieve from delivery.")
        print("Data should begin with expiry date in the format of ddmmyyyy and quantity")
        print("to each hub B1, Y1, R1, B2, Y2, R2 respectively separated by commas.")
        print("Example: 21112024, 6, 6, 6, 6, 6, 6\n")

        delivery_input = input("Enter your data here:\n")

        delivery_data = delivery_input.split(",")
        
        if validate_delivery_data(delivery_data):
            print("Data is valid!")
            break

    update_worksheet(delivery_data, "delivery")
    update_worksheet(delivery_data, "inventory")
    get_expiry_date_of_delivery_to_update_usage_wastage_sheet(delivery_data)
    
    return delivery_data

def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")

def get_expiry_date_of_delivery_to_update_usage_wastage_sheet(data):
    """
    Get expiry date of new delivery to update usage and wastage worksheet
    """
    new_expiry_date = data[0]
    new_expiry_date_to_update_usage_wastage = [new_expiry_date, '0', '0', '0', '0', '0', '0']

    update_worksheet(new_expiry_date_to_update_usage_wastage, "remove_by_using")
    update_worksheet(new_expiry_date_to_update_usage_wastage, "remove_by_wasting")
    
    return new_expiry_date_to_update_usage_wastage

def remove_item_by_usage():
    """
    Collect usage data from user to calculate usage in respective area, by using data collect to help 
    locate cell coordinate to be updated. The data collected is also used to update inventory worksheet.
    """

    date_input_value = expiry_date_of_milk_used_or_wasted()

    area_value = area_of_milk_used_or_wasted()

    number_bottle_value = quantity_of_milk_used_or_wasted()

    usage_worksheet = SHEET.worksheet('remove_by_using')
    coordinate1 = usage_worksheet.find(date_input_value)
    row = coordinate1.row
    coordinate2 = usage_worksheet.find(area_value)
    column = coordinate2.col

    cell_value = int(usage_worksheet.cell(row, column).value)

    new_cell_value = cell_value + number_bottle_value

    usage_worksheet.update_cell(row, column, new_cell_value)

    print("Remove_by_using wroksheet updated successfully....\n")

    inventory_worksheet = SHEET.worksheet('inventory')
    coordinate3 = inventory_worksheet.find(date_input_value)
    row = coordinate3.row
    coordinate4 = inventory_worksheet.find(area_value)
    column = coordinate4.col

    cell_value_inv = int(inventory_worksheet.cell(row, column).value)

    new_cell_value_inv = cell_value_inv - number_bottle_value

    inventory_worksheet.update_cell(row, column, new_cell_value_inv)

    print("Inventory wroksheet updated successfully....\n")

def remove_item_by_wastage():
    """
    Collect wastage data from user to calculate wastage in respective area, by using data collect to help 
    locate cell coordinate to be updated. The data collected is also used to update inventory worksheet.
    """
    date_input_value = expiry_date_of_milk_used_or_wasted()

    area_value = area_of_milk_used_or_wasted()

    number_bottle_value = quantity_of_milk_used_or_wasted()

    wastage_worksheet = SHEET.worksheet('remove_by_wasting')
    coordinate1 = wastage_worksheet.find(date_input_value)
    row = coordinate1.row
    coordinate2 = wastage_worksheet.find(area_value)
    column = coordinate2.col

    cell_value = int(wastage_worksheet.cell(row, column).value)

    new_cell_value = cell_value + number_bottle_value

    wastage_worksheet.update_cell(row, column, new_cell_value)

    print("Remove_by_wasting wroksheet updated successfully....\n")

    inventory_worksheet = SHEET.worksheet('inventory')
    coordinate3 = inventory_worksheet.find(date_input_value)
    row = coordinate3.row
    coordinate4 = inventory_worksheet.find(area_value)
    column = coordinate4.col

    cell_value_inv = int(inventory_worksheet.cell(row, column).value)

    new_cell_value_inv = cell_value_inv - number_bottle_value

    inventory_worksheet.update_cell(row, column, new_cell_value_inv)

    print("Inventory wroksheet updated successfully....\n")

def expiry_date_of_milk_used_or_wasted():
    """
    Request the expiry date of the milk used or wasted from user
    """
    while True:
        print("Please enter expiry date of milk to be used or wasted (ddmmyyyy)")

        date_input = input("Please enter expiry date here:\n")

        if validate_date_input(date_input):
            print(f"The date you entered is {date_input}\n")
            print("Date is valid!\n")
            break

    return date_input

def area_of_milk_used_or_wasted():
    """
    Request the area that is milk is used or wasted from user
    """
    while True:
        print("Please enter the location for the milk to be used or wasted")

        area = input("Please enter area here:\n")

        if validate_area_input(area):
            print(f"The area entered is {area}\n")
            print("Area is valid!\n")
            break

    return area

def quantity_of_milk_used_or_wasted():
    """
    Request the number of bottle used or wasted from the user
    """
    while True:
        print("Please enter the number of bottle of milk used or wasted")

        number_of_bottle = int(input("Please enter the number of bottle here:\n"))

        if validate_number_of_bottle_input(number_of_bottle):
            print(f"The number of bottle entered is {number_of_bottle}\n")
            print("The number is valid!\n")
            break

    return number_of_bottle
    
def view_wastage():
    print("You are viewing the wastage data")
   
def validate_delivery_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 7 values.
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
    Inside the try, converts string value into integer.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 8 values.
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
    Inside the try, check if value entered is not in the dictionary and raises ValueError if not. 
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
    Inside the try, check if the value entered is equal to 0 if it is then ValueError is raised
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
