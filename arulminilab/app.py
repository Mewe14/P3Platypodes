from flask import Blueprint, render_template, request
from arulminilab.bubblem import arulbubble

manuelminilab_bp=Blueprint('arulminilab_bp', __name__ ,

                           template_folder = '../arulminilab/templates',
                           static_folder='static', static_url_path='assets')



@arulminilab_bp.route('/bubblem' , methods=['GET', 'POST'])
def bubble():
    sort = 0
    listy = ""
    if request.method == 'POST':
        value = request.form['list']
        m = arulbubble
        sort = m.sort_original(value)
        listy = m.bubbleSort(value)

    return render_template("/arulminilab/minilabtesting.html", sort=sort, listy=listy)

