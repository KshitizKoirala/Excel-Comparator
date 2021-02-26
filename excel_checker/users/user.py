import os
import pandas as pd
from flask import current_app
from excel_checker.extensions import db


# User Model
class User(db.Model):
    __tablename__ = "UserTable"

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50), nullable=False)
    branch = db.Column(db.String(50), nullable=False)
    boid = db.Column(db.String(50), nullable=True)
    phoneNumber = db.Column(db.BigInteger(), unique=True, nullable=True)
    ucc_code = db.Column(db.BigInteger(), nullable=False)
    client_code = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"('{self.fullname}', '{self.phoneNumber}', '{self.boid}', '{self.branch}', '{self.ucc_code}', '{self.client_code}')"
