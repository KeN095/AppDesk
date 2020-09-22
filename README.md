# AppDesk
AppDesk, short for Appointment Desk, is a CRUD app made in Flask that allows user to create, search for, update and delete appointments with pre-selected doctors in a basic calendar-GUI

**Create**: Asks user for basic information and stores it in a database

**Search**: Search for appointment using an appointment ID, and display the contents of the appointment on the same page

**Update**: Updating information on users appointment if made already

**Delete**

# Todo

**Create**

    
- [ ] Make calendar dynamic as user changes the months in the header. Make the system know when the start of the month and the end of the month should actually start and end on the calendar grid 

- [ ] Grey out the days up until today in the calendar grid. For example: grey out all the cells from September 1st to today and make them unclickable so the user can not use the date  

- [ ] Fix highlighting issue in each cell (Originally it almost occupied the cell, now an added css rule gives a rectangle highlight in the cell)

- [ ] Have a confirm page to see if details are correct

- [ ] Input verification in HTML and python


**Search**

- [ ] Define how users with no session will be handled in page (Either redirect to search page if not in session or through login page)

- [ ] Establish forgotten appointment ID to retrieve user appointment details

- [ ] Destroy data on search page if search was already made so that it isnt persistent through page refresh


**Update**

- [ ] Decide if the update page should be it's own page or should extend the create page

- [ ] Redirect to search/login page if the user is not in session

- [ ] Show confirm page to have user confirm details

**Database**

- [ ] Reduce attributes in database (Eliminate phone number, InsuranceID) and add in a date time attribute

- [ ] Further testing

**Other**

- [ ] Clean up code

- [ ] Variable renaming

- [ ] Add CSS

- [ ] Emailing (for confirming any appointment action, reminder before appointment, and retrieving lost appointment ID)

- [ ] Maybe determine if inputted email is valid

- [ ] Add in message flashing

- [ ] Define how long session data is valid for (Should be valid as long as you are on the tab)

**Pages**

* Create - For creating appointments, also the landing page (Extends home)

* Search - For retrieving appointment information by inputting appointment ID (Extends home)

* Confirm - For confirming appointment details and any appointment action (Extends home)

* Success - For showing users action was done sucessfully (Extends home)

* Update - For updating appointments (Extends create or it uses create with textbox prefilled from data from database)

* Home - empty page/a template to extend of off

**Page routes**

**Create**

Create.html :arrow_right: Confirm.html :arrow_right: Success.html

**Delete**

Delete.html :arrow_right: Confirm.html  :arrow_right: Success.html

*If no appointment in session*

Delete.html :arrow_right: Search/login.html :arrow_right: Delete.html :arrow_right: Confirm.html :arrow_right: Success.html



**Search**

Search.html

*If no appointment in session*

Search.html :arrow_right: Search/login.html :arrow_right: Search.html 


**Update**

Create.html :arrow_right: Search/login.html :arrow_right: Create.html :arrow_right: Success.html

*If no appointment in session*
    
Create.html :arrow_right: Search/login.html :arrow_right: Create.html :arrow_right: Confirm.html :arrow_right: Success.html

**Database**

* firstName - Users first name, used to address the user in app

* lastName - Users last name, used to address the user in app

* Appointment ID - Randomly generated 6 digit ID used to identify the users appointment. Primary key.

* Email - Users email. Used for delivering appointments actions (confirmation, deleting and updating appointments) and retrieving forgotten appointment ID's

* Date/time - The date/time of the users appointment. Can be used in send out the reminder email.

* Doctor - The appointed doctor for the users appointment.

* ~~Phone number - Users point of contact. Almost has no use in the app so it can be trashed~~

* ~~Extra notes - Extra notes the user can inform of for their appointment. Almost has no use in app.~~

* ~~Insurance ID - The users insurance ID number. Almost has no use in the app other than a secondary unique key in identifying a person~~

Total attributes: 9
Idle attributes: 3
Useful attributes: 6




