from flask import Flask, render_template, redirect, request
# import the class from friend.py
from user import User

app = Flask(__name__)

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    # friends = Friend.get_all()
    # print(friends)
    return render_template("users.html", all_users = User.get_all())

@app.route("/user/new")
def new_user():
    return render_template("new_user.html")

@app.route("/users")
def user_table():
    return render_template("users.html", all_users = User.get_all())

@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True,port=5001)    