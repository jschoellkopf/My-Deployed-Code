#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    user_info = request.form
    order_time = datetime.now()
    total_fruits = int(user_info["strawberry"]) + int(user_info["raspberry"]) + int(user_info["apple"])
    print(f"Charging {user_info['first_name']} for {total_fruits} fruits")
    return render_template("checkout.html", user_info = user_info, total_fruits = total_fruits, order_time = order_time.strftime("%B %d %Y at %I:%M%p")) 

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True,port=5001)    