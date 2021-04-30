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
    #return render_template("/minilab/testpage.html")