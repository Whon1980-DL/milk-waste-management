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

    CHOICE = int(input("Select choice:"))
    print(f"The choice selected is {CHOICE}")


get_user_choice()