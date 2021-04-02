from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, session, redirect, url_for, g
import os
from classes.app import classes_bp
from club.app import club_bp
from sports.app import sports_bp
from teacher.app import teacher_bp
from administration.app import administration_bp

app = Flask(__name__)
app.register_blueprint(classes_bp, url_prefix='/classes')
app.register_blueprint(club_bp, url_prefix='/club')
app.register_blueprint(sports_bp, url_prefix='/sports')
app.register_blueprint(teacher_bp, url_prefix='/teacher')

''' database setup  '''
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "userprofiles.db"))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)


#@app.route('/')
#@app.route('/landing', methods=["GET", "POST"])
#def landing_page():
   # users = None

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5001")