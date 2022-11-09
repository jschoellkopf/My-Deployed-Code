from flask import Flask, render_template, request, redirect, session
import random
# from datetime import datetime
app = Flask(__name__)  

app.secret_key = "banana"

@app.route('/')         
def index():
    if "target" not in session:
        session["target"] = random.randint(1,100)
        session["count"] = 0
        session['limit'] = 7
    print(session['target'])
    print(session['count'])
    return render_template("index.html")

@app.route('/guessed', methods = ["POST"])
def guessed():
    if int(request.form['var_num']) == session['target']: # THIS NEEDS TO HAVE THE PRIORITY OVER THE ATTEMPTS FAILURE
            session['result'] = "success"
            session['count'] += 1
            return render_template("guess.html")

    elif session['count']+1 >= session['limit']:
        session['result'] = 'fail'
        return render_template("guess.html")

    elif int(request.form['var_num']) > session['target']:
        session['result'] = 'high'
        session['count'] += 1
        return render_template("guess.html")

    elif int(request.form['var_num']) < session['target']:
        session['result'] = 'low'
        session['count'] += 1
        return render_template("guess.html")
    

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True,port=5001)    

#decoding cookie from inspect - application - cookies - taking value all the way to but excluding the ".", and open python shell
# python3
# >>> import base64
# >>> base64.urlsafe_b64decode('eyJjb3VudCI6NywibnVtX3JlbG9hZHMiOjN9===')
# b'{"count":7,"num_reloads":3}'
# >>>