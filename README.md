# AppDesk
AppDesk, short for Appointment Desk, is a CRUD app made in Flask that allows user to create, search for, update and delete appointments with pre-selected doctors in a basic calendar-GUI

<b>Create</b>: Asks user for basic information and stores it in a database

<b>Search</b>: Search for appointment using an appointment ID, and display the contents of the appointment on the same page

<b>Update</b>: Updating information on users appointment if made already

<b>Delete</b>


# Todo

**Create**

    
        * Make calendar dynamic as user changes the months in the header. Make the system know when the start of the month and the end of the month should actually start and end on the calendar grid </li>

        * Grey out the days up until today in the calendar grid. For example: grey out all the cells from September 1st to today and make them unclickable so the user can not use the date </li> 

        * Fix highlighting issue in each cell (Originally it almost occupied the cell, now an added css rule gives a rectangle highlight in the cell)
        * Have a confirm page to see if details are correct
        * Input verification in HTML and python


**Search**

        * Define how users with no session will be handled in page (Either redirect to search page if not in session or through login page)

        * Establish forgotten appointment ID to retrieve user appointment details


**Update**

        * Decide if the update page should be it's own page or should extend the create page
        * Redirect to search/login page if the user is not in session
        * Show confirm page to have user confirm details

**Database**
        * Reduce attributes in database (Eliminate phone number, InsuranceID) and add in a date time attribute
        * Further testing

**Other**
        * Clean up code
        * Variable renaming
        * Add CSS

