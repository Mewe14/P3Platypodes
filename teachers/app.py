import os
from flask import Flask, Blueprint, render_template, flash, redirect, url_for, session, logging
from flask import request
from teachers.sort import teacher


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

teachers_bp = Blueprint('teachers', __name__,
                       template_folder='templates',
                       static_folder='static', static_url_path='assets')

@teachers_bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return render_template("allteacher.html", teach=teacher(int(request.form.get("series"))))
    return render_template("allteacher.html", teach=teacher(1))