from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)  

app.secret_key = "banana_split"

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/postresults', methods = ["POST"])
def postresults():
    session['name'] = request.form['var_name']
    session['location'] = request.form['var_location']
    session['language'] = request.form['var_language']
    study_t = ""
    for i in request.form.getlist('study_time'):
        study_t += f"{i} "
    session['study_time'] = study_t
    session['food'] = request.form['var_food']
    session['comment'] = request.form['var_comment']
    return redirect("/results")

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True,port=5001)    
