from flask import Flask, render_template, url_for, request, redirect, session, flash
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.secret_key = "a random string"
db = SQLAlchemy(app)

class appointment(db.Model):
    aptID = db.Column(db.String(6), primary_key = True, nullable = False)
    insuranceID = db.Column(db.String(10), nullable = False)
    firstName = db.Column(db.String(20), nullable = False)
    lastName = db.Column(db.String(20), nullable = False)
    phoneNumber = db.Column(db.String(16), nullable = False)
    email = db.Column(db.String(40), nullable = False)
    doctor = db.Column(db.String(40), nullable = False)
    notes = db.Column(db.String(300), nullable = True)
    #aptDatetime_db = db.Column(db.String(45), nullable = False)

    def __init__(self, aptID, insuranceID, firstName, lastName, phoneNumber, email, doctor, notes):
        self.aptID = aptID
        self.insuranceID = insuranceID
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.email = email
        self.doctor = doctor
        self.notes = notes
'''
@app.route('/')

def index():
    return render_template('home.html')
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('create.html', days = ['Sun', 'Mon','Tue','Wed','Thu','Fri','Sat'] )

@app.route('/success', methods=['GET', 'POST'])
def success():
        if request.method == 'POST':
        
            firstName = request.form['fName']
            lastName = request.form['lName']
            insuranceID = request.form['insuranceID']
            doctor = request.form['doctors']
            phone_number = request.form['phoneNum'] 
            email = request.form['email'] 
            extraInfo = request.form['extranotes']
            aptID = random.randint(100000, 999999)
            
            #push request.form data into appointment object instead of storing them into variables

            try: 
        
                new_apt = appointment(aptID, insuranceID, firstName, lastName, phone_number, email, doctor, extraInfo)

                db.session.add(new_apt)
                db.session.commit()
                
                session['patient'] = firstName
                session['lastName'] = lastName
                session['phoneNum'] = phone_number
                session['aptID'] = aptID
                session['doctor'] = doctor
                session['insuranceID'] = insuranceID
                session['email'] = email
                session['extraInfo'] = extraInfo


                #fix redirecting with parameters
                return render_template('success.html')
                #return render_template('success.html', ID = session["aptID"], lastname = session['lastName'], doc = session['doctor'])
                #if there is an error, it is because the primary key, the insurance ID, is the same in the database

            except:
                return 'There was an issue adding your appointment to the system. Please make sure all your details are correct'   
        if "lastName" in session:
            return render_template('success.html')
        else:
            #flash("You have not yet made an appointment.")
            return redirect(url_for('index'))

@app.route("/delete", methods = ['GET','POST'])
def delete():
    '''
    check if data is in session, if it is, redirect to delete page
    if not, redirect to search page

    search page should either return all appointments by name and insurance ID
    or return one appointment based on appointment ID and ask if appoinment wants to be cancelled
    '''
    if "lastName" in session:
        try:
            #appointment_to_delete = appointment.query.filter_by(aptID = session["aptID"]).first()
            #above statement works for querying based on primary key

            
            appointment.query.filter_by(aptID = session["aptID"]).delete()
            db.session.commit()

            doctor = session['doctor']

            #db.session.delete(appointment_to_delete)
            

            #also test if data still exists after deleting the row by inserting it into delete html page

            
            session.pop("lastName",None)
            session.pop("aptID",None)
            session.pop("doctor",None)
            session.pop("insuranceID",None)
            session.pop("email",None)
            session.pop("extraInfo",None)
            
            
            return render_template('delete.html', doctor = doctor)
        except:
            return "Unable to delete data. Try again."

@app.route("/update", methods = ['GET','POST'])
def update():
    #try to utilize create page

    if "patient" in session:
        return render_template("update.html")
    else:
        return redirect(url_for('index'))


@app.route("/search", methods = ['GET','POST'])
def search():
    if request.method == 'POST':
        aptID = request.form['aptSearch']
      
        try:
            info = appointment.query.filter_by(aptID = aptID).first()
            return render_template('search.html', info = info)
        
        except:
            return "Something went wrong.."
    
    else:
        return render_template("search.html")

#email confirmation
#input checking
#input patient data into database

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)