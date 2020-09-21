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

>Delete.html :arrow_right: Confirm.html  :arrow_right: Success.html

>>If no appointment in session

>>Delete.html :arrow_right: Search/login.html :arrow_right: Delete.html :arrow_right: Confirm.html :arrow_right: Success.html



**Search**

Search.html

If no appointment in session

Search.html :arrow_right: Search/login.html :arrow_right: Search.html 


**Update**

Create.html :arrow_right: Search/login.html :arrow_right: Create.html :arrow_right: Success.html

If no appointment in session
    
Create.html :arrow_right: Search/login.html :arrow_right: Create.html :arrow_right: Confirm.html :arrow_right: Success.html



