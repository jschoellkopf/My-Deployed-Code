from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)  

app.secret_key = "banana_split"

@app.route('/')         
def index():
    if "gold" not in session:
        session['gold'] = 0
        session['log'] = []
        session['count'] = 0
        session['moves'] = 10
        session['target'] = 100
    return render_template("index.html")

@app.route('/process_money', methods = ["POST"])
def postresults():

    dictionary_buildings = {
        "farm": [10,20],
        "cave": [5,10],
        "house": [2,5],
        "casino": [-50,50],
    }

    # farm
    if request.form['building'] in dictionary_buildings:
        print(dictionary_buildings[request.form['building']][0])
        gold = random.randint(dictionary_buildings[request.form['building']][0],dictionary_buildings[request.form['building']][1])
        if gold < 0:
            color = "red"
        else:
            color = "green"
        session['gold'] += gold
        session['log'].insert(0,[f"Earned {gold} gold from the {request.form['building']}! {datetime.now().strftime('%Y/%m/%d %I:%M %p')}",color])
        session['count'] += 1
    
    # # farm
    # if request.form['building'] == "farm":
    #     gold = random.randint(10,20)
    #     if gold < 0:
    #         color = "red"
    #     else:
    #         color = "green"
    #     session['gold'] += gold
    #     session['log'].insert(0,[f"Earned {gold} gold from the {request.form['building']}! {datetime.now().strftime('%Y/%m/%d %I:%M %p')}",color])
    #     session['count'] += 1
    # 
    # # cave
    # if request.form['building'] == "cave":
    #     gold = random.randint(5,10)
    #     if gold < 0:
    #         color = "red"
    #     else:
    #         color = "green"
    #     session['gold'] += gold
    #     session['log'].insert(0,[f"Earned {gold} gold from the {request.form['building']}! {datetime.now().strftime('%Y/%m/%d %I:%M %p')}",color])
    #     session['count'] += 1

    # # house
    # if request.form['building'] == "house":
    #     gold = random.randint(2,5)
    #     session['gold'] += gold
    #     if gold < 0:
    #         color = "red"
    #     else:
    #         color = "green"
    #     session['log'].insert(0,[f"Earned {gold} gold from the {request.form['building']}! {datetime.now().strftime('%Y/%m/%d %I:%M %p')}",color])
    #     session['count'] += 1

    # # casino
    # if request.form['building'] == "casino":
    #     gold = random.randint(-50,50)
    #     session['gold'] += gold
    #     if gold < 0:
    #         color = "red"
    #     else:
    #         color = "green"
    #     session['log'].insert(0,[f"Earned {gold} gold from the {request.form['building']}! {datetime.now().strftime('%Y/%m/%d %I:%M %p')}",color])
    #     session['count'] += 1

    return redirect("/")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True,port=5001)    
