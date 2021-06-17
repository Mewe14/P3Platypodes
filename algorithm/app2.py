from flask import Blueprint, render_template, request
from algorithm.testing import sophiebubble

minilab_bp=Blueprint('minilab_bp',__name__,

                     template_folder = 'templates',
                     static_folder='static', static_url_path='assets')



@minilab_bp.route('/testing' , methods=['GET', 'POST'])
def testingminilab():
    sorty = 0
    list = ""

    if request.method == 'POST':
        value = request.form['list']
        k = sophiebubble
        sorty = k.sorty_original(value)
        list = k.bubbleSort(value)

        return render_template("/minilab/testpage.html", sorty=sorty, list=list)

