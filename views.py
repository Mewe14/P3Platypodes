@app.route('/quiz')
def Quiz():
    return render_template("quiz.html")
@app.route('/Responses/')
def Responses():
    return render_template("Responses.html")