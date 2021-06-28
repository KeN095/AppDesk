from flask import Flask, render_template, url_for, request, redirect, flash, session
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from forms import AppointmentForm, LookUpForm
import random
import calendar

app = Flask(__name__)
app.config["SECRET_KEY"] = "dGhpcyBpcyBzdXBwb3NlZCB0byBiZSBhIHNlY3JldCBrZXkgYnV0IGlmIHlvdSBnb3QgaGVyZSBjb25ncmF0dWxhdGlvbnMK"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SESSION_TYPE'] = 'sqlalchemy'

db = SQLAlchemy(app)

app.config['SESSION_SQLALCHEMY'] = db

sess = Session(app)

details = {
        "First name": None,
        "Last name": None,
        "Appointment ID": None,
        "Doctor": None,
        "Email": None
    }

class appointment(db.Model):
    aptID = db.Column(db.String(6), primary_key = True, nullable = False)
    firstName = db.Column(db.String(20), nullable = False)
    lastName = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(40), nullable = False)
    doctor = db.Column(db.String(40), nullable = False)
    #aptDatetime_db = db.Column(db.String(45), nullable = False)

    def __init__(self, aptID, firstName, lastName, email, doctor):
        self.aptID = aptID
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.doctor = doctor

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

'''
@app.errorhandler(Exception)
def handle_exception(e):
    return render_template("500.html")

@app.route('/', methods=['GET', 'POST'])
def index():
    form = AppointmentForm()
    #appointment creation page that passes in the days of the week as an array for the calendar table
    return render_template('create.html', form = form)
'''

def pop():
    session.pop("First name", None)
    session.pop("Last name",None)
    session.pop("Appointment ID",None)
    session.pop("Doctor",None)
    session.pop("Email",None)
    session.pop('csrf_token', '')

#use this function to figure out why the search -> update -> search bug is happening
def displaySession():
   for key in session:
       print(key + ": " + session[key] + "\n")

    
@app.route('/', methods = ['GET', 'POST'])
def create():
    if request.method == 'POST':
            #If the user fills out the form, then the details from the form is assigned into the variables and is asigned a 6 digit appointment ID
            firstName = request.form['firstName']
            lastName = request.form['lastName']
            doctor = request.form['doctors']
            email = request.form['email'] 
            aptID = random.randint(100000, 999999)

            try: 
                #New object is created to store in database
                new_apt = appointment(aptID, firstName, lastName, email, doctor)

                #Data will be stored when it is commited

                db.session.add(new_apt)
                db.session.commit()
                
                #Establishing session by storing credentials in the session after successful database operation. Can be used to determine if redirects take place
                #session['patient']= True
                session['First name'] = firstName
                session['Last name'] = lastName
                session['Appointment ID'] = aptID
                session['Doctor'] = doctor
                session['Email'] = email

                #fix redirecting with parameters
                #flash message here
                return render_template('success.html')
                #return render_template('success.html', ID = session["aptID"], lastname = session['lastName'], doc = session['doctor'])
                #if there is an error, it is because the primary key, the insurance ID, is the same in the database

            except:
                #If there is a failure in entering in appointment data then the message below will be displayed
                return 'There was an issue adding your appointment to the system. Please make sure all your details are correct'   
    if "Last name" in session:
        #Shows the same succcess page if user is in the session
        return render_template('success.html')
    else:

        print("\n" + calendar.month(2020, 12))
        
        #If no session data exists then display the page normally
        form = AppointmentForm()
        return render_template('create.html', form = form)
    

    form = AppointmentForm()

    return render_template('create.html', form = form)

@app.route('/success', methods=['GET', 'POST'])
def success():

    if "patient" not in session:
        return redirect(url_for('create'))

    return render_template('succcess.html')

    
    #This portion is reached from the form in the create page
        
#debug purposes only, shows all of database
@app.route("/views")
def views():
    return render_template("views.html", appointments = appointment.query.all())           

@app.route("/delete", methods = ['GET','POST'])
def delete():
    #This page can delete a users appointment
        #First checks if the user is in session and if they are, then enter in the try block
        try:
            if "Last name" in session:
            #appointment_to_delete = appointment.query.filter_by(aptID = session["aptID"]).first()
            #above statement works for querying based on primary key

                #Finding the appointment ID by using the appointmentID in the session and then deleting that
                appointment.query.filter_by(aptID = session["Appointment ID"]).delete()
                db.session.commit()

                doctor = session['Doctor']
                #setting doctor variable equal to the one in session to display it in the next page
                
                #Once appointment is deleted then pop all data from session
                
                session.pop("First name",  None)
                session.pop("Last name", None)
                session.pop("Appointment ID", None)
                session.pop("Doctor", None)
                session.pop("Email", None)
                session.pop('csrf_token', '')

            elif details.get("Appointment ID") is not None:
                appointment.query.filter_by(aptID = details["Appointment ID"]).delete()
                db.session.commit()
            
                doctor = details['Doctor']

                for key in details:
                    details[key] = None    
            
            
            return render_template('delete.html', doctor = doctor)
        except:
            #Below message is displayed if appointment was unable to be deleted
            return "Unable to delete data. Try again."
    
        return redirect(url_for('search'))

@app.route("/update", methods = ['GET','POST'])
def update():
    #Below block of code is only reached when user submits their updated info
    if request.method == "POST":
        try:
            if "Last name" in session:
                info = appointment.query.filter_by(aptID = session["Appointment ID"]).first()
            else:
                info = appointment.query.filter_by(aptID = details["Appointment ID"]).first()
                
            info.firstName = request.form['firstName']
            info.lastName = request.form['lastName']
            info.email = request.form['email']
            
            db.session.commit()

            if "Last name" in session:
                session['First name'] = request.form['firstName']
                session['Last name'] = request.form['lastName']
                session['Email'] = request.form['email']
            else:
                details['First name'] = request.form['firstName']
                details['Last name'] = request.form['lastName']
                details['Email'] = request.form['email']

            

        except Exception as e:
            return render_template("500.html", error = e)

    #try to utilize create page

    #Incomplete but allows to update appointment information
    #incomplete but flash message here 

    form = AppointmentForm()

    # Also has to be checked if a user has a session but also looks up another appointment and tries to edit that instead

    #If user visits the update page, then their information is filled in the fields
    if "Last name" in session:
        
        form.firstName.data = session['First name']
        form.lastName.data = session['Last name']
        form.email.data = session['Email']
        #form.doctors.data = session['Doctor']

        #displaySession()
        #print("Update went into session")
        return render_template("update.html", form = form)
    
    elif details.get("Appointment ID") is not None:
        #If user looks up their appointment details first and selects the edit option from there, then the details 
        #will get passed into the update page and the fields will be prefilled with the information
        form.firstName.data = details['First name']
        form.lastName.data = details['Last name']
        form.email.data = details['Email']
        #form.doctors.data = session['Doctor']

        #displaySession()
        #print("Update went into details")

        return render_template("update.html", form = form)
    else:
        #If there is no information to fill in the fields, then redirect to the search page
        return redirect(url_for('search'))


@app.route("/search", methods = ['GET','POST'])
def search():
    #Allows to obtain appointment information by inputting appointment ID
    form = LookUpForm()
    #Key:Value
    #To get key names:names in details print details
    #To get value: details[names]

    if form.validate_on_submit():
        form.idSearch.data = ""
        #If the user enters an appointment ID, then assign the aptID to the value that was entered in
        aptID = request.form['idSearch']
      
        #set info equal to the object obtained in database

        try:
        
            info = appointment.query.filter_by(aptID = aptID).first()

            details["First name"] = info.firstName
            details["Last name"] = info.lastName
            details["Appointment ID"] = info.aptID
            details["Doctor"] = info.doctor
            details["Email"] = info.email

            #Pass in dictonary object 'details' for easier iterations
            return render_template('search.html', form = form, details = details)
        except Exception as e:
            return render_template("404.html", error = e)

    else:
        #Search page is displayed if visited normally
        '''

        There are different ways to search for someones appointment:
        In the search page you can display someones appointment if they enter the right appointment ID.
        Since appointment ID, are unique only to use, there could be a chance someone else could know that.
        The issue is how would you verify someones identity, if changes were made to an appointment, through another piece of personal information that only the user knows
        or by sending an email, something which the user only has access to.
        If done by another piece of personal information, then the insurance ID attribute should be added to the database

        On arrival of search page, there are checks made in jinja.
        If the user is not in the session, then show the appointment ID field.
        If they are in the session then display a table filled with the appointment details and display
        2 additional buttons to either update their appointment details or cancel it

        If the user is not in the session and inputs an appointment ID to search for and is valid, then display the details for the appointment
        '''
        '''
        if "First name" in session:

            currentSession = {

                "First name": session['First name'],
                "Last name": session['Last name'],
                "Appointment ID": session['Appointment ID'],
                "Doctor": session['Doctor'],
                "Email": session['Email'] 

            }
            return render_template("search.html", form = form, CS = currentSession)
        '''
        #displaySession()
        return render_template("search.html", form = form)
        

if __name__ == "__main__":
    #create db file if none exists
    db.create_all()
    app.run(debug=True)