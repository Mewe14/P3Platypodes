from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, session, redirect, url_for, g
import os

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

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5001")