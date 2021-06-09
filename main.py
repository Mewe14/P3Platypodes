from flask import Flask, render_template, request, session

app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask import render_template, request, redirect, url_for
import os
from classes.app import classes_bp
from clubs.app import clubs_bp
from minilab.app import minilab_bp
from quiz import quiz_data
from sports.app import sports_bp
from algorithm.app import algorithm_bp
from query import query_colleges
from custom import apology, convert
from werkzeug.security import generate_password_hash


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

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        formUser = request.form["username"]  # using name as dictionary key
        resultproxy = db.engine.execute(
            text("SELECT * FROM users WHERE username=:username;").execution_options(autocommit=True),
            username=formUser)

        user = convert(resultproxy)

        # troubleshooting
        if user == False:
            return render_template("login.html", error=True)

        # set the user id
        session.clear()
        session["user_id"] = user["id"]

        # redirects us to the user page
        return redirect(url_for("user1", usr=user["username"]))
    else:
        return render_template("login.html", error=False)


@app.route("/<usr>")
def user1(usr):
    # compute rows
    resultproxy = db.engine.execute(
        text("SELECT * FROM users WHERE username=:username;").execution_options(autocommit=True),
        username=usr)

    user = convert(resultproxy)
    if user == False:
        user = {'id': 404, 'username': 'iDontExist',
                'hash': 'password hash',
                'name': 'That user does not exist!', 'bio': "You probably typed a name in the search bar. The user "
                                                            "you searched for either doesn't exist or deleted their "
                                                            "account"}
    return render_template("profile.html", user=user)


@app.route('/newuser/', methods=["GET", "POST"])
def new_user():
    """Register user"""
    if request.method == "POST":
        # Make sure they put in their username
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Make sure they put in a password
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Make sure the passwords match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords must match", 403)

        fullname = request.form.get("name")
        print(request.form.get("bio") == '')

        # Insert all the values into the database
        db.engine.execute(
            text("INSERT INTO users (username, hash, name, bio) VALUES (:user, :hash, :name, :bio);").execution_options(
                autocommit=True),
            user=request.form.get("username"),
            hash=generate_password_hash(request.form.get("password")),
            name=fullname, bio=request.form.get("bio"))

        return redirect("/login")
    else:
        return render_template("signup.html")


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        newuser = request.form["newusername"]  # using name as dictionary key
        # redirects us to the user page
        return redirect(url_for("newuser", newusr=newuser))
    else:
        return render_template("signup.html")


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
    return render_template("Responses.html")

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


@app.route('/profile')
def profile():
    # compute rows
    resultproxy = db.engine.execute(text("SELECT * FROM users WHERE id=:id;").execution_options(autocommit=True),
                                    id=session["user_id"])

    user = convert(resultproxy)
    return render_template("profile.html", user=user)



if __name__ == "__main__":
    app.run(debug=True, port="5003")