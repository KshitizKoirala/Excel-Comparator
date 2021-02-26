# The Interaction part between the database is commented as these are working ideas.
# These are working pieces of code so feel free to pull and play around

from excel_checker import create_app

# custom packages to load the database
# from config.config import config

# STRING CONFIGURATION TO LOAD THE DATABASE CREDENTIALS IN F STRINGS
# f'{os.getenv("DB_DIALECT")}://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}/{os.getenv("DB_NAME")}'


# create_app function to initialize the excel_checker application database and then run the app
app = create_app()
if __name__ == '__main__':
    app.run(debug=True)


# LOADING CONFIGURATION FROM THE DATABASE
# import os
# from flask import Flask, redirect, url_for, flash, request, render_template
# from wtforms import Form, StringField, IntegerField, FileField, validators
# from flask_sqlalchemy import SQLAlchemy

# connecting to the database
# db = config(app)


# Upload Excel Files Model
# class Excelfiles(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     ComparedExcel = db.Column(db.String(100), nullable=False)
#     comapred_excel_data = db.Column(db.LargeBinary, nullable=False)

#     def __repr__(self):
#         return f"('{self.BankExcel}', '{self.TmsExcel}')"

# GET ALL METHOD
# @app.route('/getexcel', methods=['GET'])
# def get_excel_files():
#     files = Excelfiles.query.all()
#     return render_template('get_excel.html', file=files)
