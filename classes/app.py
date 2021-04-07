import os
from flask import Flask, Blueprint, render_template, flash, redirect, url_for, session, logging
from flask import request
from classes.sort import mathematics


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

classes_bp = Blueprint('classes', __name__,
                       template_folder='templates',
                       static_folder='static', static_url_path='assets')


@classes_bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return render_template("allclass.html", math=mathematics(int(request.form.get("series"))))
    return render_template("allclass.html", math=mathematics(1))