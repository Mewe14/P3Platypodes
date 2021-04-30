from flask import Blueprint, render_template, request
from minilab.testing import bubblesorting

minilab_bp=Blueprint('minilab',__name__,
                     template_folder = 'templates',
                     static_folder='static')



@minilab_bp.route('/testing' , methods=['GET', 'POST'])
def testingminilab():
    g = 0
    list = ""
    if request.method == 'POST':
        value = request.form['list']
        k = bubblesorting
        g = k.g_original(value)
        list = k.bubbleSort(value)
    return render_template("/minilab/testpage.html", g=g, list=list)
