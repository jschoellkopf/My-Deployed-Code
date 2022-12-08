from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

# HOME PAGE
@app.route('/dojos') #base home page route
def index():
    all_dojos = Dojo.get_all()
    print(all_dojos)
    return render_template("index.html",all_dojos = all_dojos)
    # for home page, we need the dojos to showcase each one of them

@app.route('/create_dojo',methods=['POST']) #submits create dojo form from home page
def create_dojo():
    data = {
        "name":request.form['name'],
    }
    Dojo.save(data)
    return redirect('/dojos')

#--------------------------------
# DOJO PAGE

@app.route('/dojo/<int:dojo_id>') #takes you to particular dojo
def detail_page(dojo_id):
    data = {
        'id': dojo_id
    }
    all_ninjas = Ninja.get_all_ninjas_from_one_dojo(dojo_id)
    return render_template("dojo.html",dojo=Dojo.get_one(data),all_ninjas = all_ninjas)
    # if you click on one of the dojos, it takes you to who is in it

#EDIT NINJA
@app.route('/user/edit/<int:ninja_id>/<int:dojo_num>') #from dojo page takes you to edit ninja
def edit_page(ninja_id,dojo_num): #using dojo_num to store dojo_id
    data = {
        'id': ninja_id
    }
    all_dojos = Dojo.get_all()
    return render_template("edit_page.html", ninja = Ninja.get_one(data),all_dojos = all_dojos, dojo_num=dojo_num)
    #using dojo_id as variable given from the edit link because we want to come back to same dojo after deletion

@app.route('/update/<int:ninja_id>', methods=['POST']) #process form of update ninja
def update(ninja_id):
    data = {
        'id': ninja_id,
        "first_name":request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age'],
        "dojo_id": request.form['dojo_id']
    }
    Ninja.update(data)
    return redirect('/dojo/'+f"{request.form['dojo_id']}")

@app.route('/user/delete/<int:ninja_id>/<int:dojo_id>') #delete and redirects to dojo where ninja was
def delete(ninja_id,dojo_id):
    data = {
        'id': ninja_id,
    }
    Ninja.destroy(data)
    return redirect('/dojo/'+f"{dojo_id}")

# -------------------------------------
# ADDING NINJA PAGE

@app.route('/add_ninja') #adding ninja page
def new_ninja():
    all_dojos = Dojo.get_all()
    return render_template('add_ninja.html',all_dojos = all_dojos)
    # adding ninjas, we need to pass in the different dojos to allow the selection from the list, like above in /dojos

@app.route('/create_ninja',methods=['POST']) #creating ninja process and redirecting to ninja's Dojo
def create_ninja():
    data = {
        "first_name":request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age'],
        "dojo_id": request.form['dojo_id']
    }
    Ninja.save(data)
    return redirect('/dojo/'+f"{request.form['dojo_id']}")

# --------------------------------------


