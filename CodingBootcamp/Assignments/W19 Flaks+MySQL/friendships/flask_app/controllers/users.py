from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def home():
    return redirect('/friendships')

@app.route('/friendships') #base home page route
def friendships():
    return render_template("index.html", users = User.get_users(), friends = User.get_friends(),all_users = User.get_all())

@app.route('/add_user',methods=['POST'])
def add_user():
    data = {
        "first_name":request.form['first_name'],
        "last_name": request.form['last_name'],
    }
    User.save(data)
    return redirect('/')

@app.route('/add_friendship',methods=['POST'])
def add_friendship():
    data = {
        "user_id":request.form['user_id'],
        "friend_id": request.form['friend_id'],
    }
    User.add_friendship(data)
    return redirect('/')