from flask import Flask, Blueprint, render_template
from flask import request


algorithm_bp = Blueprint('algorithm', __name__,
                         template_folder='../algorithm/templates',
                         static_folder='static', static_url_path='assets')

algorithm = Flask(__name__)


@algorithm_bp.route('/', methods=["GET", "POST"])
def algorithm():
    if request.method == 'POST':
        print(request.method)
        a=int(request.form.get("a"))
        b=int(request.form.get("b"))

        from math import gcd

        class LeastCommonMultiple:

            def __init__(self, a,b):
                self._multiple = self.lcm()
                self._denominator = self.gcd()

            def gcd(self):
                if a == 0:
                    return b
                return gcd(b % a, a)

            # Function to return LCM of two numbers
            def lcm(self):
                return (a / gcd(a,b))* b

            @property
            def leastcommon_multiple(self):
                return self._multiple

            @property
            def denominator(self):
                return self._denominator


        # Driver program to test above function
        LeastCommonMultiple = LeastCommonMultiple(a,b)

        return render_template("sophieminilab.html", a=a, b=b, lcm=LeastCommonMultiple.leastcommon_multiple, gcd=LeastCommonMultiple.denominator)
    return render_template("sophieminilab.html")