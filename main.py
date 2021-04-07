from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, session, redirect, url_for
from flask import request
import os
from classes.app import classes_bp
from clubs.app import clubs_bp
from sports.app import sports_bp
from algorithm.app import algorithm_bp
#from teachers.app import teachers_bp
#from administration.app import administration_bp

app = Flask(__name__)
app.register_blueprint(classes_bp, url_prefix='/classes')
app.register_blueprint(clubs_bp, url_prefix='/clubs')
#app.register_blueprint(teachers_bp, url_prefix='/teachers')
app.register_blueprint(sports_bp, url_prefix='/sports')
app.register_blueprint(algorithm_bp, url_prefix='/algorithm')


''' database setup  '''
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "userprofiles.db"))
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/minilabs')
def Minilabs():
    return render_template('minilabs.html')




if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5001")