# Milk Waste Management Application

Today sustainability is at the heart of everything we do and decided on. Food waste reduction is one of the main ways an organisation or community needs to practice and highly regard in order for it to be sustainable. Being sustainable also resulted in carbon emission reduction and hence following the concept of the "New World" we live in. 

Milk Waste Management application is designed to aid an organisation or community to meet sustainable goal. The application allow for easy recording of data and thus provide data that is readily available for analysis and drawing up plan that is data driven to gear an organisation towards be sustainable. 

The application is designed to automate editing a google spreadsheet stored on cloud platform that any users with access can view and obtain the stored data for further analysis. User will be able to view inventory, record delivery, record usage, record wastage and record any inventory movement within usage areas through a terminal. Furthermore the ease of use of the application will make waste management and recoding process fun and simple!

![Main Menu](readme_images/main_menu.png)

[View Milk Waste Management Application live project here](https://milk-waste-management-5ea677ef764f.herokuapp.com/)

[View Milk Waste Management Google Sheets here](https://docs.google.com/spreadsheets/d/1SSIEZcKAZLnjjF3mJlnYxwPEvKTbCURKLN882PISL-U/edit?usp=sharing)

## Table of Contents
### [How to use](#how-to-use-1)
### [Logic Flowchart](#logic-flowchart-1)
### [User Experience (UX)](#user-experience-ux-1)
* [User Stories](#user-stories)
### [Design](#design-1)
### [Features](#features-1)
* [Existing Features](#existing-features)
### [Features Left to Implement](#features-left-to-implement-1)
### [Technologies Used](#technologies-used-1)
### [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used-1)
### [Testing](#testing-1)
### [Manual Testing](#manual-testing-1)
### [Input validation testing](#input-validation-testing-1)
### [Fixed Bugs](#fixed-bugs-1)
### [Deployment](#deployment-1)
* [Deployment to Heroku](#deployment-to-heroku)
* [Forking the GitHub Repository](#forking-the-github-repository)
* [Local Clone](#local-clone)
### [Credits](#credits-1)
* [Code](#code)
* [Content](#content)
### [Acknowledgements](#acknowledgements-1)
---

## How to Use

Through Milk Waste Management Application, user can view milk inventory data recoded on linked Google Sheet, record milk delivery, record milk wastage and record milk movement between usage area in a building. The user will be presented with choices they have to select in order to perform certain action. For recording action, user will be prompted to enter data along with guideline on how the data should be entered. The application will also provide respective error messages to guid user to correctly input valid data which will then lead to the selected action being performed to the Google Sheet.

## Logic Flowchart

![Flowchart](readme_images/logic_flowchart.png)

## User Experience (UX)

The application provided user with clear introduction of the idea behind the design of the application with main menu and instruction to what action should be taken to proceed. Once user selected an action the application will display data or request data as appropriate. The data is displayed in a format that is very easy to understand by the user. The data provided by user is validate with several methods to ensure data provided is valid and of correct format and pattern. The application notify user every time a task is perform successfully and what worksheet has been updated. It is a very simple yet highly capable application to help simplify milk waste management process. 

### User Stories

* First-time visitor goals
    * Understand how to use the application. Clear introduction and instructions are given. Understand the valid format of data be requested through understanding displayed error messages.
    * Use the application. Once the user understands the application, they will likely want to use it.
    * Enjoy the experience. The application should be simple and beneficial to the user. 

* Returning visitor goals
    * Continue using. The returning visitor may have enjoyed using the application and wants to use again.
    * Share with friends and colleagues. Recommend colleagues to give the applcaition a try.
    * Exploring new features, if there is any update. 

* Frequent user goals
    * Switched to updating the spreadsheet through the application over manual updating.
    * Organisation made the use of application mandatory for all employees.
    * Increasing productivity can be seen from using the application.
    * Accuracy of input data is evident.
    * Reduction in wastage amount is evident after a certain period of application usage.
    * Exploring new features, if there is any update.

---

### Design

* Colours
    * White font to make it easy to see on black background of the terminal.
    * Black background that come with the build-in terminal

* instruction and confirmation
    * Instructions given at every steps of the application usage.
    * Data provided is confirmed back to user to indicate that the application is progressing.

* Flowchart
    * [Lucidchart](https://www.lucidchart.com/)

---

### Features

* Introduction to the idea behind the design of the application is clearly provided. In what environment is the application built for.
* Provided choices to allow user to select with of the choice for exiting the application.
* Clear instruction on what data is required to perform selected action and in what format it needs to be provided.
* Error messages help guild user towards providing valid data in order for application to proceed to the next step.
* Data display is very easy to understand and user friendly. 

### Existing Features

* Welcome screen
    * Display welcome message with an introduction of the application as well as main menu.

![Welcome Screen](readme_images/main_menu.png)

* Google sheet
    * The application is linked to a specific Google sheet and is allowed to edit the sheet.

![Google Sheet](readme_images/linked_google_sheet.png)

* View inventory menu
    * if choice 1 of the main menu is selected, the submenu to view inventory is displayed and prompt user to select further choice.

![Submenu](readme_images/submenu.png)

* View Full Inventory
    * If choice 1 of submenu is selected, the application will display a full inventory.

![Full Inventory](readme_images/full_inventory.png)

* View Inventory of Specific Date
    * If choice 2 of the submenu is selected, the application will request the expiry date they want to see from the user.
    * The application then display the inventory of the specific date provided by the user.

![Request for Expiry Date to View](readme_images/request_specific_date_to_view.png)

![Inventory of Specific Date](readme_images/inventory_of_specific_date.png)

* Exit From Submenu
    * If choice 3 of the submenu is selected, the user will be directed back to main menu.

* Record Delivery
    * If choice 2 of the main menu is selected, the application will request user for delivery data to use for updating worksheets accordingly.The application will also notify user once relevant worksheets are updated.
    * The application will also insert the new expiry date onto remove_by_using and remove_by_wasting worksheets with quantity of 0 for each location for future used.

![Request for Delivery Data](readme_images/request_for_delivery_data.png)
![Notification of Worksheets Successfully Updated](readme_images/notification_of_worksheet_successfully_updated.png)

* Record Usage
    * if choice 3 of the main menu is selected, the application will request the expiry date of the milk they will use and the location the milk will be used and how many bottle will be used form the user. The data provided then used to calculate and update remove_by_using and inventory worksheets. 

![Request Usage Data for Updating Usage Worksheet](readme_images/request_usage_data.png)
![Notification of Worksheets Successfully Updated for Usage](readme_images/notification_of_usage_updated.png)

* Record Wastage
    * If choice 4 of the main menu is selected, the application will request the expiry date of the milk they will waste and the location the milk will be wasted and how many bottle will be wasted form the user. The data provided then used to calculate and update remove_by_wasting and inventory worksheets.

![Request Usage Data for Updating Wastage Worksheet](readme_images/request_wastage_data.png)
![Notification of Worksheets Successfully Updated for Wastage](readme_images/notification_of_wastage_updated.png)

* Record Redistribution
    * If the user wants to record the redistribution of inventory in the case when milk expiry date is soon due and there are still a lot of milk of that expiry date left in certain location that consume less to a location that only has milk that will expire later as all the one soon to expired have been consumed, the user can select choice 5. 
    * When choice 5 is selected, the application will request expiry date of milk the user wants to redistribute, the location redistribute from, quantity of milk redistributing and location milk is redistribute to. The application then update the relevant worksheets with the data provided for accuracy of milk movement recording. 

![Request Redistribution data for Updating inventory Worksheet](readme_images/request_redistribution_data1.png)
![Request Redistribution data for Updating inventory Worksheet Continue](readme_images/request_redistribution_data2.png)
![Notification of Successful Calculation and Worksheet sucessfully updated](readme_images/notification_redistribution.png)

* Exit application
    * If choice 6 is selected, the application will display Exiting and exit the application. 

## Features Left to Implement

* Option to calculate average 5 days usage for next milk order.
* Validation to check and reject if user enter expiry date that has passed the use-by-date for recording delivery.
* Function to automatically erase inventory entry with 0 quantity or expiry date older than current date.
* Function to provide statistic of wastage. 

---

## Technologies Used

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

---

## Frameworks, Libraries & Programs Used

* [Gitpod](https://www.gitpod.io/)
    * To write the code.
* [Git](https://git-scm.com/)
    * for version control.
* [Github](https://github.com/)
    * Deployment of the website and storing the files online.
* [Lucidchart](https://www.lucidchart.com/)
    * To create a logic flowchart of the application.
* [Heroku](https://www.heroku.com/)
    * To deploy the project.
* [CI Python Linter](https://pep8ci.herokuapp.com/)
    * Check code for any issues.
* [Google Sheets](https://docs.google.com/)
    * To create and store spreadsheet online

---

## Testing 

CI Python Linter was used to test run.py.

<details>
<summary> run.py CI Python Linter check
</summary>

![run.py linter check](readme_images/python_linter_check.png)
</details>

## Manual Testing

The application was manually tested extensively using Gitpod terminal, and once the website was deployed on Heroku it was manually tested again, during the creation of the code to the end. Testing of choices display, delivery data input validation, expiry date input validation, location usage and wastage input validation, quantity of milk input validation, data input for milk redistribution and finally the updating of relevant google spreadsheets.

| Feature | Expected Result | Steps Taken | Actual Result | 
| ------- | -------------- | ----------- | ------------- | 
| Welcome Screen   | To display welcome message, introduction and Main Menu | Select choice | As Expected | 
| Select choice 1 of Main Menu | To display view inventory options | Select choice  | As Expected |
| Submenu | Prompt user to select inventory options | Select choice | As Expected |
| View Full Inventory Options | To display full inventory | Select choice 1 | As Expected |
| View Specific Date Inventory   | Request for expiry date of interest | Input expiry date | As Expected |
| Expiry Date doesn't exist   | To display date doesn't exist | Input expiry date that doesn't already exist in the inventory | As Expected |
| Display Specific Date Inventory   | Display the inventory of the specific date input | none | As Expected |
| Return to Main Menu   | To return to Main menu | Select choice 3 | As Expected |
| Record Delivery   | To request for delivery data | Input delivery data | As Expected |
| Invalid Date input  | To display date input is invalid, not follow dd-mm-yyyy format | Input date with wrong format | As Expected |
| Invalid day value   | To display day provided is incorrect | Input day bigger than 31 | As Expected |
| Invalid month value   | To display month provided is incorrect | Input day bigger than 12 | As Expected |
| Invalid year value   | To display year provided is in valid | Input year other than 2024 and 2025 | As Expected |
| Record Milk Usage   | To request for usage data | Input date, location and quantity data | As Expected |
| Invalid location value   | To display location provided is not valid | Input location other than B1, Y1, R1, B2, Y2, R2 | As Expected |
| Record Milk Wastage   | To request for wastage data | Input date, location and quantity data | As Expected |
| Quantity to remove more than availability  | To display the quantity to move cannot exceed what is available in the inventory | Input quantity that exceed the quantity in the inventory | As Expected |
| Record Milk Redistribution   | Request for expiry date, location from, quantity and location to  | Input redistribution data  | As Expected |
| Exit application  | To exit from application | Select option 6 of the Main Menu | As Expected |

## Input validation testing

* Menu choice
    * Cannot continue with empty input
    * Cannot continue with 0 input
    * Must be number between 1 - 6

![Empty String Choice](readme_images/empty_string_choice.png)
![Zero Value Choice](readme_images/zero_value_choice.png)
![Alphabetic Choice](readme_images/alphabetic_choice.png)
![Two Digits Choice](readme_images/more_than_one_digit_choice.png)
![More Than Six Choice](readme_images/more_than_six_choice.png)
![Valid Choice](readme_images/valid_choice.png)

* Delivery data
    * Must have 7 values
    * Date must follow dd-mm-yyyy format
    * Day must be number between 1 - 31
    * Month must be number between 1 - 12
    * Year must be 2024 or 2025
    * Quanity for each location cannot exceed 100 units

![Delivery Data More Than 7 Values ](readme_images/delivery_data_morea_than_7_value.png)
![Delivery Data Missing First Dash](readme_images/delivery_data_missing_first_dash.png)
![Delivery Data Missing Second Dash](readme_images/delivery_data_missing_second_dash.png)
![Delivery Data Day Too Big](readme_images/delivery_data_day_too_big.png)
![Delivery Data Day Zero](readme_images/delivery_data_day_zero.png)
![Delivery Data Month Too Big](readme_images/delivery_data_month_too_big.png)
![Delivery Data Month Zero](readme_images/delivery_data_month_zero.png)
![Delivery Data Year Invalid](readme_images/delivery_data_invalid_year.png)


* Expiry date data for removing 
    * Must be of 10 characters
    * Must follow dd-mm-yyyy format
    * Must be date that is already exist in the inventory
    * Day must be number between 1 - 31
    * Month must be number between 1 - 12
    * Year must be 2024 or 2025

![Expiry Date More Than 10 Characters](readme_images/ex_date_more_than_10_char.png)
![Expiry Date Missing First Dash](readme_images/ex_date_miss_first_dash.png)
![Expiry Date Missing Second Dash](readme_images/ex_date_miss_second_dash.png)
![Expiry Date Day Too Big](readme_images/ex_date_day_too_big.png)
![Expiry Date Day Zero](readme_images/ex_date_day_zero.png)
![Expiry Date Month Too Big](readme_images/ex_date_day_too_big.png)
![Expiry Date Month Zero](readme_images/ex_date_day_zero.png)
![Expiry Date Year Invalid](readme_images/ex_date_year_invalid.png)
![Expiry Date Dosenot Exist](readme_images/ex_date_doesnot_exist.png)

* Location data for removing and redistributing
    * Cannot be anything else other than B1, Y1, R1, B2, Y2, R2

![Location Data Invalid](readme_images/location_data_invalid.png)

* Milk quantity data for removing and redistributing 
    * Cannot continue with empty input
    * Cannot continue with 0 input
    * Quantity to move from or remove cannot exceed what is available in the inventory for any respective locations

![Milk Quantity Data Empty](readme_images/quantity_data_empty.png)
![Milk Quantity Data Zero](readme_images/quantity_data_zero.png)
![Milk Quantity Data More Than Available](readme_images/quantity_data_more_than_available.png)

## Fixed Bugs

* When using range of index of list to test for date validation, index number used were incorrect and was later correct.
* When locating cell location on a spreadsheet column value were incorrect and had to subtract 1 to correct it to select correct entry to display when viewing specific date inventory in particular.
* User input had to be converted to integer using int() before it can be compared with value on the spreadsheet.
* Value on usage and wastage for entry with expiry date cannot be empty and has contain zero for future quantity calculation. Thus expiry and 0 value of quantity had to be parsed to usage and wastage every time after delivery is recorded. 

## Deployment

### Deploying to Heroku

To deploy with Heroku, Code Institute Python Essentials Template was used so the python code can be viewed in a terminal in a browser
1. Log in to Heroku or create a new account
2. On the main page click "New" and select "Create new app"
3. Choose your unique app name and select your region
4. Click "Create app"
5. On the next page find "settings" and locate "Config Vars"
6. Click "Reveal Config Vars" and add "PORT" key and value "8000", click "Add"
7. Scroll down, locate "Buildpack" and click "Add", select "Python"
8. Repeat step 7. only this time add "Node.js", make sure "Python" is first
9. Scroll to the top and select "Deploy" tab
10. Select GitHub as deployment method and search for your repository and link them together
11. Scroll down and select either "Enable Automatic Deploys" or "Manual Deploy"
12. Deployed site [Milk Waste Management Application](https://milk-waste-management-5ea677ef764f.herokuapp.com/)

### Forking the GitHub Repository

By forking the repository, we make a copy of the original repository on our GitHub account to view and change without affecting the original repository by using these steps:

1. Log in to GitHub and locate [GitHub Repository Milk Waste Management](https://github.com/Whon1980-DL/milk-waste-management)
2. At the top of the Repository(under the main navigation) locate "Fork" button.
3. Now you should have a copy of the original repository in your GitHub account.

### Local Clone

1. Log in to GitHub and locate [GitHub Repository Milk Waste Management](https://github.com/Whon1980-DL/milk-waste-management)
2. Under the repository name click "Clone or download"
3. Click on the code button, select clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone` and then paste The URL copied in the step 3.
7. Press Enter and your local clone will be created.

## Credits

### Code

* I gained understanding of python through code institute lessons.
* I gained more python concepts through Python for begginers presented by Telusko on YouTube.
* Python 3.11.3 documentation.
* MDN web docs for python [Documentation](https://developer.mozilla.org/en-US/docs/Glossary/Python).

### Content

* Milk Waste Management.
* All content was written by the developer.

## Acknowledgements

 * My mentor Mitko Bachvarov provided helpful feedback.
 * Slack community for encouragement.
 * My wife, Nan,  for her full support and my 2 sons, Dylan and Logan, who have been very encouraging.