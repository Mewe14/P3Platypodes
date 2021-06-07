from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import requests
app = Flask(__name__)

""" database locations """
dbURI = 'sqlite:///createDB'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)

"""
Sample of table creation and data population
"""

"""DB creation"""
engine = create_engine(dbURI)
session = Session(bind=engine)


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    country = db.Column(db.String(255), unique=False, nullable=False)
    state = db.Column(db.String(255), unique=False, nullable=False)
    address = db.Column(db.String(255), unique=False, nullable=False)
    zip = db.Column(db.String(255), unique=False, nullable=False)
    website = db.Column(db.String(255), unique=False, nullable=False)


if __name__ == "__main__":
    """create each table"""
    db.create_all()

    # api2 code implemented into database table
    url = "https://universities-and-colleges.p.rapidapi.com/universities"

    querystring = {"page": "1", "includeUniversityDetails": "true", "countryCode": "US", "limit": "50", "state": "true", "address": "true", "website": "true", "zip": "true"}

    headers = {
        'x-RapidAPI-Key': "7060fafea1mshc1031ccdb460c56p1e6e83jsnc95eba373c88",
        'x-RapidAPI-Host': "universities-and-colleges.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    list = response.json()

    try:
        for item in list:
            #          print(item["name"], item["countryCode"])
            u1 = Users(name=item["name"], country=item["countryCode"], state=item["state"], address=item["address"], zip=item["zip"], website=item["website"])
            session.add_all([u1])
        session.commit()


    except:
        print("Records exist")

    print("Table: Users")
    list = Users.query.all()
    for row in list:
        print(row.user_id)
        print(row.name)
        print("country:", row.country)
        print("state:", row.state)
        print("address:", row.address)
        print("zip code:", row.zip)
        print("website:", row.website)