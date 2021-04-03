import os
from flask import Flask, Blueprint, render_template, flash, redirect, url_for, session, logging
from flask import request
from sports.sort import sports


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

sports_bp = Blueprint('sports', __name__,
                       template_folder='templates',
                       static_folder='static', static_url_path='assets')

@sports_bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return render_template("allsports.html", sports=sports(int(request.form.get("series"))))
    return render_template("allsports.html", sports=sports(1))