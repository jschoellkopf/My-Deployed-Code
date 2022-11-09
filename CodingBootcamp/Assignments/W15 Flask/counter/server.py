from flask import Flask, render_template, request, redirect, session
# from datetime import datetime
app = Flask(__name__)  

app.secret_key = "banana"

@app.route('/')         
def index():
    if "count" not in session:
        session["count"] = 1
        session["num_reloads"] = 1
    else:
        session["count"] += 1
        session["num_reloads"] += 1
    return render_template("index.html")

@app.route('/+2')
def plus_two():
    session["count"] += 1
    return redirect('/')

@app.route('/add', methods = ["POST"])
def add_var_num():
    session["count"] += (int(request.form['var_num'])-1)
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.pop('count')
    return redirect('/')


if __name__=="__main__":   
    app.run(debug=True,port=5001)    

#decoding cookie from inspect - application - cookies - taking value all the way to but excluding the ".", and open python shell
# python3
# >>> import base64
# >>> base64.urlsafe_b64decode('eyJjb3VudCI6NywibnVtX3JlbG9hZHMiOjN9===')
# b'{"count":7,"num_reloads":3}'
# >>>