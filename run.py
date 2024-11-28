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
        print("(4) Record Wastage.                                  ")
        print("(5) Record Redistribution.                           ")
        print("(6) Exit.                                            ")
        print("=====================================================")

        choice = input("Enter your choice by entering number 1 to 6:\n")

        validate_choice_input(choice)

        if choice == '1':
            """
            Allow user to chose to view full inventory or inventory of specific date 
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
                    specific_inventory = view_specific_date_inventory()
                    print(specific_inventory)
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
    Display full inventory to user, using for loop to make data displayed more user friendly.
    """
    inventory_worksheet = SHEET.worksheet('inventory')
    inventory_data = inventory_worksheet.get_all_values()

    for inventory_data in inventory_data:
        print (*inventory_data, sep ='  ')
    
    print("\n")

def view_specific_date_inventory():
    """
    Display inventory of item of specific date according to the expiry date user provide.
    """
    print("Please enter expiry date of the the milk you'd like to view (ddmmyyyy)")

    date_input_value = expiry_date_of_milk()
    
    inventory_worksheet = SHEET.worksheet('inventory')
    coordinate1 = inventory_worksheet.find(date_input_value)
    row = coordinate1.row

    data = SHEET.worksheet("inventory").get_all_values()[row - 1]
    headings = SHEET.worksheet("inventory").get_all_values()[0]

    return {heading: data for heading, data in zip(headings, data)} 

def add_item_from_delivery():
    """
    Collect delivery data from user to update delivery and inventory worksheet
    and run a funciton to get expiry date to use with usage and wastage worksheet.
    """
    while True:

        print("Please enter date and quantity of item recieve from delivery.")
        print("Data should begin with expiry date in the format of ddmmyyyy and quantity")
        print("to each hub B1, Y1, R1, B2, Y2, R2 respectively separated by commas.")
        print("Example: 21112024, 6, 6, 6, 6, 6, 6\n")

        delivery_input = input("Enter your data here:\n")

        delivery_data = delivery_input.split(",")

        print(delivery_data)
        
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
    print("Please enter expiry date of the milk to be used (ddmmyyyy)")
    date_input_value = expiry_date_of_milk()
    print("Please enter the location (B1 or Y1 or R1 or B2 or Y2 or R2) for the milk to be used")
    area_value = area_of_milk_removed_or_added()
    print("Please enter the number of milk bottle to be used")
    number_bottle_value = quantity_of_milk_removed_or_added()

    add_inventory_to_worksheet(date_input_value, area_value, number_bottle_value, "remove_by_using")
    remove_inventory_from_worksheet(date_input_value, area_value, number_bottle_value, "inventory")

    return 

def remove_item_by_wastage():
    """
    Collect wastage data from user to calculate wastage in respective area, by using data collect to help 
    locate cell coordinate to be updated. The data collected is also used to update inventory worksheet.
    """
    print("Please enter expiry date of the milk to be wasted (ddmmyyyy)")
    date_input_value = expiry_date_of_milk()
    print("Please enter the location (B1 or Y1 or R1 or B2 or Y2 or R2) for the milk to be wasted")
    area_value = area_of_milk_removed_or_added()
    print("Please enter the number of milk bottle to be wasted")
    number_bottle_value = quantity_of_milk_removed_or_added()

    add_inventory_to_worksheet(date_input_value, area_value, number_bottle_value, "remove_by_wasting")
    remove_inventory_from_worksheet(date_input_value, area_value, number_bottle_value, "inventory")

    return

def record_redistribution():
    """
    Allow user to enter data to record redistribution of milk between usage areas and update inventory worksheet accordingly
    """
    print("Please enter expiry date of the milk to be redistributed (ddmmyyyy)")
    date_input_value = expiry_date_of_milk()
    print("Please enter the location where milk is taken from")
    area_value_from = area_of_milk_removed_or_added()
    print("Please enter the number of milk bottle being redistributed")
    number_bottle_value = quantity_of_milk_removed_or_added()
    print("Please enter the location where milk is taken to")
    area_value_to = area_of_milk_removed_or_added()

    remove_inventory_from_worksheet(date_input_value, area_value_from, number_bottle_value, "inventory")
    add_inventory_to_worksheet(date_input_value, area_value_to, number_bottle_value, "inventory")
    
    print(f"{number_bottle_value} bottle(s) of milk has been subtracted from {area_value_from} and added to {area_value_to} successfully...\n")
    print("Inventory worksheet updated successfully....\n")

    return

def add_inventory_to_worksheet(date, area, quantity, worksheet):
    """
    Use value input by user to locate cell row and column to perform addition to.
    """
    worksheet_to_add = SHEET.worksheet(worksheet)
    coordinate1 = worksheet_to_add.find(date)
    row = coordinate1.row
    coordinate2 = worksheet_to_add.find(area)
    column = coordinate2.col
    cell_value = int(worksheet_to_add.cell(row, column).value)
    new_cell_value = cell_value + (quantity)
    worksheet_to_add.update_cell(row, column, new_cell_value)
   
    return print(f"{worksheet} worksheet updated successfully....\n")

def remove_inventory_from_worksheet(date, area, quantity, worksheet):
    """
    Use value input by user to locate cell row and column to perform subtraction from.
    """
    worksheet_to_remove_from = SHEET.worksheet(worksheet)
    coordinate1 = worksheet_to_remove_from.find(date)
    row = coordinate1.row
    coordinate2 = worksheet_to_remove_from.find(area)
    column = coordinate2.col
    cell_value = int(worksheet_to_remove_from.cell(row, column).value)
    new_cell_value = cell_value - (quantity)
    worksheet_to_remove_from.update_cell(row, column, new_cell_value)

    return print(f"{worksheet} worksheet updated successfully....\n")

def expiry_date_of_milk():
    """
    Request the expiry date of the milk the user is dealing with.
    """
    while True:
       
        date_input = input("Please enter expiry date here:\n")

        if validate_date_input(date_input):
            print(f"The date you entered is {date_input}\n")
            print("Date is valid!\n")
            break

    return date_input

def area_of_milk_removed_or_added():
    """
    Request the area that is milk is removed or added from the user
    """
    while True:

        area = input("Please enter area here:\n")

        if validate_area_input(area):
            print(f"The area entered is {area}\n")
            print("Area is valid!\n")
            break

    return area

def quantity_of_milk_removed_or_added():
    """
    Request the number of milk bottle removed or added from the user
    """
    while True:

        number_of_bottle = int(input("Please enter the number of bottle here:\n"))

        if validate_number_of_bottle_input(number_of_bottle):
            print(f"The number of bottle entered is {number_of_bottle}\n")
            print("The number is valid!\n")
            break

    return number_of_bottle

def validate_choice_input(value):
    """
    Inside the try, raises ValueError if value input is an empty string.
    """
    try:
        if value == " ":
            raise ValueError(
                f"Input value can not be empty"
            )
        if len(value) != 1:
            raise ValueError(
                f"Input value must be a single digit number, you provided {len(value)} digits number" 
            )
    except ValueError as e:
        print(f"invalid data: {e}, please try again.\n")
        return
    
    return
   
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
