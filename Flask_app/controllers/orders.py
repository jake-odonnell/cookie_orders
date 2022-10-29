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
