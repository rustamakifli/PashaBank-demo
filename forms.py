from xmlrpc.client import DateTime
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,DateField
from wtforms.validators import DataRequired,Email,Length
from wtforms_components import TimeField


class QueueForm(FlaskForm):
    name = StringField('Ad', validators=[DataRequired(),Length(max=30)])
    surname = StringField('Soyad', validators=[DataRequired(),Length(max=30)])
    number = StringField('Mobil nömrə', validators=[DataRequired(),Length(max=12)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    date = DateField('Tarix', validators=[DataRequired()])
    time = TimeField('Saat',validators=[DataRequired()])


