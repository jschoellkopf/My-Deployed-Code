from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.order import Order

@app.route("/new/order")
def new_order():
    return render_template("new_order.html")

@app.route("/orders")
def order_table():
    return render_template("orders.html", orders = Order.get_all())

@app.route("/orders/clear/session")
def clear_session():
    session['name'] = ""
    session['type'] = ""
    session['amount'] = ""
    return redirect('/orders')

@app.route('/create_order', methods=["POST"])
def create_order():
    if not Order.validate_order(request.form):
        return redirect('/new/order')
    data = {
        "name": request.form["name"],
        "type" : request.form["type"],
        "amount" : request.form["amount"],
    }
    Order.save(data)
    session['name'] = ""
    session['type'] = ""
    session['amount'] = ""
    return redirect('/orders')

@app.route('/order/edit/<int:id>')
def edit(id):
    data = {
        'id' : id
    }
    return render_template("edit_order.html", order = Order.get_one(data))

@app.route('/order/update/<int:id>', methods=["POST"])
def update(id):
    if not Order.validate_order(request.form):
        return redirect(f"/order/edit/{id}")
    Order.update(request.form)
    return redirect("/orders")

@app.route('/order/delete/<int:id>')
def delete_order(id):
    data = {
        'id' : id
    }
    Order.destroy(data)
    return redirect('/orders')
