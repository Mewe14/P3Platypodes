import os
from flask import Flask, Blueprint, render_template, flash, redirect, url_for, session, logging
from flask import request
from classes.sort import mathematics
from classes.bubble import BubbleSort
from classes.create import Create
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


@classes_bp.route('/bubblesort', methods=['GET', 'POST'])
def alphabetize():
    sort = request.form.getlist("sort")
    return render_template("bubble.html", bubbles=BubbleSort(sort))


@classes_bp.route('/create', methods=['GET', 'POST'])
def createe():
    if request.method == 'POST':
        numbers = request.form.getlist("v1")
        return render_template("create.html", nums=Create(numbers))
    return render_template("create.html", nums=Create([5, 3, 2, 1, 6]))