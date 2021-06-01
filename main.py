from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, redirect, url_for
import os
from classes.app import classes_bp
from clubs.app import clubs_bp
from minilab.app import minilab_bp
from sports.app import sports_bp
from algorithm.app import algorithm_bp

app = Flask(__name__, template_folder="Templates")
app.register_blueprint(classes_bp, url_prefix='/classes')
app.register_blueprint(clubs_bp, url_prefix='/clubs')
#app.register_blueprint(teachers_bp, url_prefix='/teachers')
app.register_blueprint(sports_bp, url_prefix='/sports')
app.register_blueprint(algorithm_bp, url_prefix='/algorithm')
app.register_blueprint(minilab_bp, url_prefix= '/minilab')
#app.register_blueprint(manuelminilab_bp, url_prefix= '/manuelminilab')

''' database setup  '''
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "userprofiles.db"))
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        return redirect(url_for("home"))
    else:
        return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for("home"))
    else:
        return render_template('login.html')


@app.route('/minilabs')
def Minilabs():
    return render_template('minilabs.html')


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/feedback')
def feedback():
    return render_template("feedback.html")


@app.route('/process')
def process():
    return render_template("process.html")

@app.route('/contact')
def process():
    return render_template("contact.html")

@app.route('/Responses/')
def Responses():
    return render_template("Responses.html")


if __name__ == "__main__":
    app.run(debug=True, port="5003")
