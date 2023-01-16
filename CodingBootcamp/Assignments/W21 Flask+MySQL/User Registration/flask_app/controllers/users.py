from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.user import User

@app.route("/")
def home():
    return render_template("new_user.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        redirect('/')
    data = {
        "id" : session['user_id']
    }
    return render_template("show_user.html", user = User.get_one(data))

@app.route('/create_user', methods=["POST"])
def create_user():
    if not User.validate_user(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/')
    # else no errors:
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : bcrypt.generate_password_hash(request.form['password']),
        "pwcheck" : bcrypt.generate_password_hash(request.form['pwcheck']),
    }
    session['user_id'] = User.save(data)
    return redirect('/dashboard')


@app.route('/login', methods=['POST'])
def login():
    # see if the email provided exists in the database
    data = {
        "email" : request.form["login_email"]
    }
    user_in_db = User.get_by_email(data)
    print(user_in_db)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password", 'login')
        # print("email doesn't exist")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['login_password']):
        # if we get False after checking the password
        flash("Invalid Email/Password", "login")
        # print('password does not match')
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    print('went through everything')
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect("/dashboard")



