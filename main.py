from flask import Flask, session

app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, redirect, url_for, g, flash
import os
from classes.app import classes_bp
from clubs.app import clubs_bp
from algorithm.app2 import algorithm_bp
from quiz import quiz_data
from sports.app import sports_bp
from algorithm.app import algorithm_bp
from query import query_colleges


app.register_blueprint(classes_bp, url_prefix='/classes')
app.register_blueprint(clubs_bp, url_prefix='/clubs')
#app.register_blueprint(teachers_bp, url_prefix='/teachers')
app.register_blueprint(sports_bp, url_prefix='/sports')
app.register_blueprint(algorithm_bp, url_prefix='/algorithm')
app.register_blueprint(algorithm_bp, url_prefix= '/algorithm')
#app.register_blueprint(manuelminilab_bp, url_prefix= '/manuelminilab')


''' database setup  '''
# project_dir = os.path.dirname(os.path.abspath(__file__))
# database_file = "sqlite:///{}".format(os.path.join(project_dir, "userprofiles.db"))
# app.config["SQLALCHEMY_DATABASE_URI"] = database_file
# db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
'''app secret key'''
app.secret_key = 'nighthawks'


@app.route('/')
def index():
    return render_template("landing.html")



class User(db.Model):
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    passwd = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"User('{self.username}')"

@app.route('/register')
def register():
    return render_template("signup.html")


# connects default URL of server to render home.html
@app.route('/signup', methods=["GET", "POST"])
def landing_page():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["passwd"]
        dbcommit = User(username = username, passwd = password)
        db.session.add(dbcommit)
        db.session.commit
        return redirect(url_for("login"))


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])
        users = User.query.all()
        session.pop("_id", None)
        try:
            user = [user for user in users if user.username == POST_USERNAME][0]
            if user and user.passwd == POST_PASSWORD:
                return render_template("landing.html")
            else:
                return redirect(url_for("login"))
                flash("incorrect username password")
        except:
            return redirect(url_for("login"))
            flash("incorrect username password")
    else:
        if "user" in session:
            return redirect(url_for("about"))
        return render_template("login.html")
    # result1 = User.query.filter(User.username == POST_USERNAME).first()
        # result2 = User.query.filter(User.passwd == POST_PASSWORD).first()


@app.route('/home')
def home_route():
    # function use Flask import (Jinja) to render an HTML template
    if g.user:
        return render_template("profile.html", user=session['user'])
    return redirect(url_for('landing'))

#@app.route('/minilabs')
#def Minilabs():
    #return render_template('minilabs.html')

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/profile')
def profile():
    return render_template("profile.html")

@app.route('/feedback')
def feedback():
    return render_template("feedback.html")

@app.route('/process')
def process():
    return render_template("process.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/quiz')
def quiz():
    return render_template("quiz.html",
                           data=quiz_data(),
                           question_index=0,
                           answers='{}')

@app.route('/Responses/')
def Responses():
    return render_template("responses.html")

@app.route('/next', methods=['POST'])
def next_question():
    print(request.form['answer'])
    print(request.form['answers'])
    print(request.form['next_question'])
    return render_template("quiz.html",
                           data=quiz_data(),
                           question_index=int(request.form['next_question']),
                           answers=request.form['answers'])


@app.route('/submit', methods=['POST'])
def submit():
    print(request.form['answers'])
    colleges = query_colleges(request.form['answers'])
    return render_template("results.html", colleges=colleges)


if __name__ == "__main__":
    db.create_all()
    db.session.commit()
    app.run(debug=True, port="5003")