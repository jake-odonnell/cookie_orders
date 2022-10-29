from Flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Order:
    def __init__(self, data:dict):
        self.id = data['id']
        self.name = data['name']
        self.cookie = data['cookie']
        self.amount = data['boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        return

    @classmethod 
    def get_all(cls):
        query = 'SELECT * from orders;'
        results = connectToMySQL('cookies').query_db(query)
        orders = []
        for order in results:
            orders.append(cls(order))
        return orders

    @classmethod
    def get_from_id(cls, data:dict):
        query = 'SELECT * FROM orders WHERE id = %(id)s;'
        result = connectToMySQL('cookies').query_db(query, data)
        return cls(result[0])

    @classmethod
    def add_order(cls, data:dict):
        query = 'INSERT INTO orders (name, cookie, boxes) VALUE (%(name)s,%(cookie)s,%(amount)s);'
        return connectToMySQL('cookies').query_db(query, data)

    @staticmethod
    def val_order(data:dict):
        is_val = True
        if len(data['name']) < 2:
            flash('Valid name is required')
            is_val = False
        if len(data['cookie']) < 2:
            flash("Valid cookie is required")
            is_val = False
        print(data['amount'])
        if data['amount'] == '' or int(data['amount']) <= 0:
            flash('Amount of Cookies must be positive number')
            is_val = False
        return is_val

    @classmethod
    def change_order(cls, data):
        query = 'UPDATE orders SET name = %(name)s, cookie = %(cookie)s, boxes = %(amount)s WHERE id = %(id)s;'
        connectToMySQL('cookies').query_db(query, data)
        return