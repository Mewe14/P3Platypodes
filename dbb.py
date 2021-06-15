from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from main import db, database_file

app = Flask(__name__)

engine = create_engine(database_file)
session = Session(bind=engine)


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    nickname = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(60), unique=True, key='email')

if __name__ == "__main__":
    """create each table"""
    db.create_all()
    try:
        u1 = Users(name='Thomas Edison', nickname='Toby', email='tedison@example.com')
        u2 = Users(name='Nicholas Tesla', nickname='Niko', email='ntesla@example.com')
        u3 = Users(name='Alexander Graham Bell', nickname='Lex', email='agbell@example.com')
        u4 = Users(name='Eli Whitney', nickname='Whit', email='eliw@example.com')
        session.add_all([u1, u2, u3, u4])
        session.commit()
    except:
        print("Records exist")

    print("Table: Users")
    list = Users.query.all()
    for row in list:
        print(row.user_id)
        print(row.name)
        print(row.nickname)
        print(row.email)