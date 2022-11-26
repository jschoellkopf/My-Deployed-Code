from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User

@app.route("/user/new")
def new_user():
    return render_template("new_user.html")

@app.route("/users")
def user_table():
    return render_template("users.html", users = User.get_all())

@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
    }
    # We pass the data dictionary into the save method from the Friend class.
    # User.save(data)
    # Don't forget to redirect after saving to the database.

    #User.save(date) returns ID from mysqlconnection whne insert
    return redirect(f'/user/show/{User.save(data)}')

@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        'id' : id
    }
    return render_template("edit_user.html", user = User.get_one(data))

@app.route('/user/show/<int:id>')
def show(id):
    data = {
        'id' : id
    }
    return render_template("show_user.html", user = User.get_one(data))

@app.route('/user/update/<int:id>', methods=["POST"])
def update(id):
    User.update(request.form)
    return redirect(f"/user/show/{id}")

# @app.route('/user/update', methods=["POST"])
# def update():
#     User.update(request.form)
#     print("hello now")
#     data = {
#         'id' : id
#     }
#     user = User.get_one(data)
#     return redirect(f"/user/show/{user.id}")

@app.route('/user/delete/<int:id>')
def delete_user(id):
    data = {
        'id' : id
    }
    User.destroy(data)
    return redirect('/users')
