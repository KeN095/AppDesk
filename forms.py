from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField
from wtforms.validators import DataRequired, Length, Email


class AppointmentForm(FlaskForm):
    firstName = StringField('First name: ', validators=[DataRequired(), Length(min = 2, max = 25)])

    lastName = StringField('Last name: ', validators=[DataRequired(), Length(min = 2, max = 25)])

    doctors = SelectField('Doctor: ', choices=[''], validators = [DataRequired()])

    email = StringField('Email: ', validators=[DataRequired(), Email()])

    submit = SubmitField('Submit')

class LookUpForm(FlaskForm):

    aptIDLookUp = StringField('Your Appointment ID: ', validators = [DataRequired(), Length(max = 6)])
    submit = SubmitField('Submit')

