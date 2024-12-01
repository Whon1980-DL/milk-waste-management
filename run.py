import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

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

        print("===========================================================")
        print("=    Welcome to DISC Milk Waste Management Application    =")
        print("===========================================================")
        print("    In a sustainable world it is also a best practice      ")
        print("   to aim for zero food waste. With the features of this   ")
        print("   application to automate data spreadsheet users can      ")
        print(" easily record and view all related data thus encouraging  ")
        print("accurate recording and readiness of data for easy analysis.")
        print("===========================================================")
        print("(1) View Inventory                                         ")
        print("(2) Receive Delivery                                       ")
        print("(3) Record Usage                                           ")
        print("(4) Record Wastage.                                        ")
        print("(5) Record Redistribution.                                 ")
        print("(6) Exit.                                                  ")
        print("===========================================================")

        choice = input("Enter your choice by entering number 1 to 6:\n")

        validate_choice_input(choice)

        if choice == '1':
            """
            Allow user to chose to view full inventory or inventory of specific date.
            """

            while True:
                print("-----------------------------------")
                print("(1) View Full Inventory")
                print("(2) View Inventory of Specific Date")
                print("(3) Back to Main menu")
                print("-----------------------------------")

                choice = input("Enter your choice here:\n")

                validate_choice_input(choice)

                if choice == '1':
                    view_full_inventory()
                elif choice == '2':
                    view_specific_date_inventory()
                elif choice == '3':
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == '2':
            add_item_from_delivery()
        elif choice == '3':
            remove_item_by_usage()
        elif choice == '4':
            remove_item_by_wastage()
        elif choice == '5':
            record_redistribution()
        elif choice == '6':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

def view_full_inventory():   
    """
    Display full inventory to user, using for loop and format() to make data displayed more user friendly.
    """
    worksheet = get_worksheet('inventory')
    inventory_data = worksheet.get_all_values()

    dash = '-' * 50

    for i in range(len(inventory_data)):
        if i == 0:
            print(dash)
            print('{:<12s}{:>6s}{:>6s}{:>6s}{:>6s}{:>6s}{:>6s}'.format(inventory_data[i][0],inventory_data[i][1],inventory_data[i][2],inventory_data[i][3], inventory_data[i][4], inventory_data[i][5], inventory_data[i][6]))
            print(dash)
        else:
            print('{:<12s}{:>6s}{:>6s}{:>6s}{:>6s}{:>6s}{:>6s}'.format(inventory_data[i][0],inventory_data[i][1],inventory_data[i][2],inventory_data[i][3], inventory_data[i][4], inventory_data[i][5], inventory_data[i][6]))
    print(dash)       

    print("\n")

def view_specific_date_inventory():
    """
    Display inventory of item of specific date according to the expiry date user provide.
    """
    while True:
        print("Please enter expiry date of the the milk you'd like to view (dd-mm-yyyy)")

        date_input_value = get_expiry_date_of_milk()

        worksheet = get_worksheet('inventory')
        inventory_data = worksheet.get_all_values()

        if validate_if_date_exist(worksheet, date_input_value):
            print("Date is valid!")
            break
    
    cell_location = worksheet.find(date_input_value)
    row = cell_location.row

    dash = '-' * 50

    for i in range(len(inventory_data)):
        if i == 0:
            print(dash)
            print('{:<12s}{:>6s}{:>6s}{:>6s}{:>6s}{:>6s}{:>6s}'.format(inventory_data[i][0],inventory_data[i][1],inventory_data[i][2],inventory_data[i][3], inventory_data[i][4], inventory_data[i][5], inventory_data[i][6]))
            print(dash)
        if i == (row - 1):
            print('{:<12s}{:>6s}{:>6s}{:>6s}{:>6s}{:>6s}{:>6s}'.format(inventory_data[i][0],inventory_data[i][1],inventory_data[i][2],inventory_data[i][3], inventory_data[i][4], inventory_data[i][5], inventory_data[i][6]))
    print(dash)       

    return 

def add_item_from_delivery():
    """
    Collect delivery data from user to update delivery and inventory worksheet
    and run a funciton to get expiry date to use with usage and wastage worksheet.
    """
    while True:

        print("Please enter date and quantity of item recieve from delivery.")
        print("Data should begin with expiry date in the format of dd-mm-yyyy and quantity")
        print("to each location B1, Y1, R1, B2, Y2, R2 respectively separated by commas.")
        print("Please note: quantity for each location cannot exceed 100 unit ")
        print("Example: 21-11-2024, 6, 6, 6, 6, 6, 6\n")

        delivery_input = input("Enter your data here:\n") 

        delivery_data = delivery_input.split(",")

        date_value = delivery_data[0]

        delivery_quantity_values = delivery_data[1:6]

        date_value_as_list = date_value.split("-")

        if validate_delivery_data(delivery_data, date_value, date_value_as_list, delivery_quantity_values):
            print("Data is valid)")
            break

    update_worksheet(delivery_data, "delivery")
    update_worksheet(delivery_data, "inventory")
    get_expiry_date_of_delivery_to_update_usage_wastage_sheet(delivery_data)
    
    return delivery_data

def get_worksheet(worksheet):
    """
    Access specific worksheet data according to the argument provided
    """
    worksheet_to_work_with = SHEET.worksheet(worksheet)

    return worksheet_to_work_with

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
    Collect usage data from user to calculate usage in respective location, by using data collect to help 
    locate cell coordinate to be updated. The data collected is also used to update inventory worksheet.
    """
    while True:
        print("Please enter expiry date of the milk to be used (dd-mm-yyyy)")

        date_input_value = get_expiry_date_of_milk()

        worksheet = get_worksheet('remove_by_using')
    
        if validate_if_date_exist(worksheet, date_input_value):
            print("Date is valid!")
            break

    print("Please enter the location (B1 or Y1 or R1 or B2 or Y2 or R2) for the milk to be used")
    location_value = get_location_of_milk_removed_or_added()
    print("Please enter the number of milk bottle to be used")
    number_bottle_value = get_quantity_of_milk_removed_or_added(date_input_value, location_value, 'inventory')

    add_inventory_to_worksheet(date_input_value, location_value, number_bottle_value, 'remove_by_using')
    remove_inventory_from_worksheet(date_input_value, location_value, number_bottle_value, 'inventory')

    return 

def remove_item_by_wastage():
    """
    Collect wastage data from user to calculate wastage in respective location, by using data collect to help 
    locate cell coordinate to be updated. The data collected is also used to update inventory worksheet.
    """
    while True:
        print("Please enter expiry date of the milk to be wasted (dd-mm-yyyy)")

        date_input_value = get_expiry_date_of_milk()

        worksheet = get_worksheet('remove_by_wasting')
    
        if validate_if_date_exist(worksheet, date_input_value):
            print("Date is valid!")
            break

    print("Please enter the location (B1 or Y1 or R1 or B2 or Y2 or R2) for the milk to be wasted")
    location_value = get_location_of_milk_removed_or_added()
    print("Please enter the number of milk bottle to be wasted")
    number_bottle_value = get_quantity_of_milk_removed_or_added(date_input_value, location_value, 'inventory')

    add_inventory_to_worksheet(date_input_value, location_value, number_bottle_value, "remove_by_wasting")
    remove_inventory_from_worksheet(date_input_value, location_value, number_bottle_value, "inventory")

    return

def record_redistribution():
    """
    Allow user to enter data to record redistribution of milk between usage locations and update inventory worksheet accordingly
    """
    while True:
        print("Please enter expiry date of the milk to be redistributed (dd-mm-yyyy)")

        date_input_value = get_expiry_date_of_milk()

        worksheet = get_worksheet('remove_by_wasting')
    
        if validate_if_date_exist(worksheet, date_input_value):
            print("Date is valid!")
            break

    print("Please enter the location (B1 or Y1 or R1 or B2 or Y2 or R2) where milk is taken from")
    location_value_from = get_location_of_milk_removed_or_added()
    print("Please enter the number of milk bottle being redistributed")
    number_bottle_value = get_quantity_of_milk_removed_or_added(date_input_value, location_value_from, 'inventory')
    print("Please enter the location (B1 or Y1 or R1 or B2 or Y2 or R2) where milk is taken to")
    location_value_to = get_location_of_milk_removed_or_added()

    remove_inventory_from_worksheet(date_input_value, location_value_from, number_bottle_value, "inventory")
    add_inventory_to_worksheet(date_input_value, location_value_to, number_bottle_value, "inventory")
    
    print(f"{number_bottle_value} bottle(s) of milk has been subtracted from {location_value_from} and added to {location_value_to} successfully...\n")
    print("Inventory worksheet updated successfully....\n")

    return

def add_inventory_to_worksheet(date, location, quantity, worksheet):
    """
    Use value input by user to locate cell row and column to perform addition to.
    """
    worksheet_to_add = SHEET.worksheet(worksheet)
    cell_location1 = worksheet_to_add.find(date)
    row = cell_location1.row
    cell_location2 = worksheet_to_add.find(location)
    column = cell_location2.col
    cell_value = int(worksheet_to_add.cell(row, column).value)
    new_cell_value = cell_value + int((quantity))
    worksheet_to_add.update_cell(row, column, new_cell_value)
   
    return print(f"{worksheet} worksheet updated successfully....\n")

def remove_inventory_from_worksheet(date, location, quantity, worksheet):
    """
    Use value input by user to locate cell row and column to perform subtraction from.
    """
    worksheet_to_remove_from = SHEET.worksheet(worksheet)
    cell_location1 = worksheet_to_remove_from.find(date)
    row = cell_location1.row
    cell_location2 = worksheet_to_remove_from.find(location)
    column = cell_location2.col
    cell_value = int(worksheet_to_remove_from.cell(row, column).value)
    new_cell_value = cell_value - int((quantity))
    worksheet_to_remove_from.update_cell(row, column, new_cell_value)

    return print(f"{worksheet} worksheet updated successfully....\n")

def get_expiry_date_of_milk():
    """
    Request the expiry date of the milk the user is dealing with.
    """
    date_input = input("Please enter expiry date here:\n")

    return date_input

def get_location_of_milk_removed_or_added():
    """
    Request the location that the milk is removed or added from the user
    """
    while True:

        location = input("Please enter location here:\n")

        if validate_location_input(location):
            print(f"The location entered is {location}\n")
            print("Location is valid!\n")
            break

    return location

def get_quantity_of_milk_removed_or_added(date, location, worksheet):
    """
    Request the number of milk bottle removed or added from the user
    """
    while True:

        number_of_bottle = input("Please enter the number of bottle here:\n")

        if validate_number_of_bottle_input(date, location, number_of_bottle, worksheet):
            print(f"The number of bottle entered is {number_of_bottle}\n")
            print("The number is valid!\n")
            break

    return number_of_bottle

def validate_choice_input(value):
    """
    Inside the try, raises ValueError if value input is an empty string or invalid choice.
    """
    try:
        if value == " ":
            raise ValueError(
                f"Input value can not be empty"
            )
        elif len(value) > 1:
            raise ValueError(
                f"Input value must be a single digit number, you provided {len(value)} digits number" 
            )
    except ValueError as e:
        print(f"invalid data: {e}, please try again.\n")
        return
    
    return

def validate_delivery_data(values, date_value, date_value_as_list, quantity):
    """
    """
    try:
        if len(values) != 7:
            raise ValueError(
                f"Exactly 7 values required with first being the expiry date (dd-mm-yyyy) then quantity for each hub separated by commas, you provided {len(values)} characters"
              )
        for x in quantity:
            if int(x) > 100:
                raise ValueError(
                    f"Quantity entered for delivery cannot exceed 100 for each location"
                )
        validate_date_input(date_value, date_value_as_list)

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

def validate_if_date_exist(worksheet, date):
    date_value_as_list = date.split("-")
    try:
        validate_date_input(date, date_value_as_list)

        if date not in worksheet.col_values(1):
            raise ValueError(
            f"Date does not exist"
        )

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True
   
def validate_date_input(date_value, date_value_as_list):
    """
    Check if date input is not empty and that date is valid
    """
    if len(date_value) != 10:
        raise ValueError(
        f"Exactly 10 characters required in the format of dd-mm-yyyy for date, you provided {len(date_value)} characters"
        )
    if date_value.find("-", 2) != 2:
        raise ValueError(
            f"A '-' is missing after value of day"
        )
    if date_value.find("-", 5) != 5:
        raise ValueError(
            f"A '-' is missing after value of month"
        )
    if date_value.count("-") != 2:
        raise ValueError(
            f"The date value require two '-' one after day and one after month, you provided {date_value.count("-")}"
        )
    if int(date_value_as_list[0]) > 31:
        raise ValueError(
            f"Date must be between 1 and 31"
        )
    elif int(date_value_as_list[0]) == 0:
        raise ValueError(
            f"Date input cannot be 0"
        )
    elif int(date_value_as_list[1]) > 12:
        raise ValueError(
            f"Month must be between 1 and 12"
        )
    elif int(date_value_as_list[1]) == 0:
        raise ValueError(
            f"Month input cannot be 0"
        )
    elif int(date_value_as_list[2]) not in {2024, 2025}:
        raise ValueError(
            f"Year eneterd is invalid"
        )
    return ValueError   

def validate_location_input(value):
    """
    Inside the try, check if value entered is not in the dictionary and raises ValueError if not. 
    """
    worksheet = get_worksheet('inventory')
    try:
        if value not in worksheet.row_values(1):
            raise ValueError(
                f"Value has to be B1 or Y1 or R1 or B2 or Y2 or R2"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True   

def validate_number_of_bottle_input(date, location, quantity, worksheet):
    """
    Inside the try, check if the quantity entered is equal to 0 if it is then ValueError is raised
    """
    worksheet_to_validate_quantity = get_worksheet(worksheet)
    cell_location1 = worksheet_to_validate_quantity.find(date)
    row = cell_location1.row
    cell_location2 = worksheet_to_validate_quantity.find(location)
    column = cell_location2.col
    cell_value_to_compare_with = int(worksheet_to_validate_quantity.cell(row, column).value)

    try:
        if int(quantity) > cell_value_to_compare_with:
            raise ValueError(
                f"Qunantity to remove cannot exceed what is available in the inventory"
            )
        if quantity == " ":
            raise ValueError(
                f"Input value can not be empty"
            )
        elif int(quantity) == 0:
            raise ValueError(
                f"Number of bottle entered must not be 0"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True   

get_user_choice()
