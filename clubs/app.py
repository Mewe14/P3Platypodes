import os
import random
from flask import Flask, Blueprint, render_template, flash, redirect, url_for, session, logging
from flask import request
from clubs import clubalgorithm

clubs_bp = Blueprint('clubs', __name__,
                     template_folder='../clubs/templates',
                     static_folder='static', static_url_path='assets')

clubs = Flask(__name__)

@clubs_bp.route('/', methods=['GET', 'POST'])
def clubs():
    if request.method == 'POST':
        newclubslist = clubalgorithm.clubslist.copy()
        featuredclubs = []

        index1 = random.choice(newclubslist)
        newclubslist.remove(index1)
        featuredclubs.append(index1)

        index2 = random.choice(newclubslist)
        newclubslist.remove(index2)
        featuredclubs.append(index2)

        return render_template("featuredclubs.html", featuredclubs=featuredclubs, clubslist=clubalgorithm.clubslist)
    return render_template("featuredclubs.html", clubslist=clubalgorithm.clubslist)