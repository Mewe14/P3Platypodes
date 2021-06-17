from flask import Blueprint, render_template, request
from algorithm.testing import sophiebubble
from flask import Flask

#minilab_bp=Blueprint('minilab_bp',__name__,

                    # template_folder = 'templates',
                     #static_folder='static', static_url_path='assets')

algorithm_bp = Blueprint('algorithm', __name__,
                         template_folder='../algorithm/templates',
                         static_folder='static', static_url_path='assets')

algorithm = Flask(__name__)




@algorithm_bp.route('/' , methods=['GET', 'POST'])
def testing():
    sorty = 0
    list = ""

    if request.method == 'POST':
        value = request.form['list']
        k = sophiebubble
        sorty = k.sorty_original(value)
        list = k.bubbleSort(value)

        return render_template("/algorithm/testpage.html", sorty=sorty, list=list)

