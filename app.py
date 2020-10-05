from flask import Flask, render_template, url_for, request, redirect, session, flash
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from forms import AppointmentForm, LookUpForm
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.secret_key = "a random string"
db = SQLAlchemy(app)

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


@app.route('/', methods=['GET', 'POST'])
def index():
    form = AppointmentForm()
    #appointment creation page that passes in the days of the week as an array for the calendar table
    return render_template('create.html', form = form)

@app.route('/success', methods=['GET', 'POST'])
def success():
    #This portion is reached from the form in the create page
        if request.method == 'POST':
            #Checks if the method of the request is POST and if it is, assign variables from the form and generate a random appointment ID
            firstName = request.form['firstName']
            lastName = request.form['lastName']
            doctor = request.form['doctors']
            email = request.form['email'] 
            aptID = random.randint(100000, 999999)
            
            #push request.form data into appointment object instead of storing them into variables

            try: 
                #In the try block, a new appointment object is created with all variables from the form 
                new_apt = appointment(aptID, firstName, lastName, email, doctor)

                #Taking the data and entering it into the database then committing that action

                db.session.add(new_apt)
                db.session.commit()
                
                #Establishing session storing credentials in the session. Can be used to determine if redirects happen or not
                session['firstName'] = firstName
                session['lastName'] = lastName
                session['aptID'] = aptID
                session['doctor'] = doctor
                session['email'] = email


                #fix redirecting with parameters
                return render_template('success.html')
                #return render_template('success.html', ID = session["aptID"], lastname = session['lastName'], doc = session['doctor'])
                #if there is an error, it is because the primary key, the insurance ID, is the same in the database

            except:
                #If there is a failure in entering in appointment data then the message below will be displayed
                return 'There was an issue adding your appointment to the system. Please make sure all your details are correct'   
        if "lastName" in session:
            #Most likely will show the same success page long after appointment was created
            return render_template('success.html')
        else:
            #flash("You have not yet made an appointment.")
            #If there is no session data then redirect to the home page to create an appointment
            return redirect(url_for('index'))

@app.route("/delete", methods = ['GET','POST'])
def delete():
    #This page can delete a users appointment
    if "lastName" in session:
        #First checks if the user is in session and if they are, then enter in the try block
        try:
            #appointment_to_delete = appointment.query.filter_by(aptID = session["aptID"]).first()
            #above statement works for querying based on primary key

            #Finding the appointment ID by using the appointmentID in the session and then deleting that
            appointment.query.filter_by(aptID = session["aptID"]).delete()
            db.session.commit()

            doctor = session['doctor']
            #setting doctor variable equal to the one in session to display it in the next page
            
            #Once appointment is deleted then pop all data from session
            session.pop("firstName", None)
            session.pop("lastName",None)
            session.pop("aptID",None)
            session.pop("doctor",None)
            session.pop("email",None)
            
            
            return render_template('delete.html', doctor = doctor)
        except:
            #Below message is displayed if appointment was unable to be deleted
            return "Unable to delete data. Try again."

@app.route("/update", methods = ['GET','POST'])
def update():
    #try to utilize create page

    #Incomplete but allows to update appointment information

    if "patient" in session:
        return render_template("update.html")
    else:
        return redirect(url_for('index'))


@app.route("/search", methods = ['GET','POST'])
def search():
    #Allows to obtain appointment information by inputting appointment ID
    if request.method == 'POST':
        #If the user inputs an appointment ID, then assign the aptID to the value that was entered in
        aptID = request.form['aptSearch']
      
        try:
            #set info equal to the object obtained in database
            info = appointment.query.filter_by(aptID = aptID).first()

            #Passing in info object, whether it is defined or not
            return render_template('search.html', info = info)
        
        except:
            return "Something went wrong.."
    
    else:
        #Search page is displayed if visited normally

        '''
        On arrival of search page, there are checks made in jinja.
        If the user is not in the session, then show the appointment ID field.
        If they are in the session then display a table filled with the appointment details and display
        2 additional buttons to either update their appointment details or cancel it

        If the user is not in the session and inputs an appointment ID to search for and is valid, then display the details for the appointment
        '''
        lookUpForm = LookUpForm()
        return render_template("search.html", form = LookUpForm())

if __name__ == "__main__":
    #create db file if none exists
    db.create_all()
    app.run(debug=True)