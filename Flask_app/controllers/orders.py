from Flask_app.models.order import Order
from Flask_app import app
from flask import redirect, request, render_template

@app.route('/')
def home():
    return redirect('/orders')

@app.route('/orders')
def r_orders():
    orders = Order.get_all()
    return render_template('orders.html', orders = orders)

@app.route('/new_order')
def r_new_order():
    return render_template('new_order.html')

@app.route('/new-order', methods = ['POST'])
def f_new_order():
    if Order.val_order(request.form):
        id = Order.add_order(request.form)
        return redirect('/orders')
    return redirect('/new_order')