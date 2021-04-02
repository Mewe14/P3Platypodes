import os
from flask import Flask, Blueprint, render_template, flash, redirect, url_for, session, logging
from flask import request
from clubs import clubalgorithm

clubs_bp = Blueprint('clubs', __name__,
                     template_folder='templates',
                     static_folder='static', static_url_path='assets')

@clubs_bp.route('/')
def index():
    return render_template('featuredclubs.html', featuredclubs=clubalgorithm.featuredclubs)
