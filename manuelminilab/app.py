from flask import Blueprint, render_template, request
from manuelminilab.bubblem import manuelbubble

manuelminilab_bp=Blueprint('manuelminilab_bp', __name__ ,

                     template_folder = '../manuelminilab/templates',
                     static_folder='static', static_url_path='assets')



@manuelminilab_bp.route('/bubblem' , methods=['GET', 'POST'])
def bubble():
    sort = 0
    listy = ""
    if request.method == 'POST':
        value = request.form['list']
        m = manuelbubble
        sort = m.sort_original(value)
        listy = m.bubbleSort(value)

    return render_template("/manuelminilab/minilabtesting.html", sort=sort, listy=listy)

