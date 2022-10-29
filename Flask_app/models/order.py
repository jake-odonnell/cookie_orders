from Flask_app.config.mysqlconnection import connectToMySQL

class Order:
    def __init__(self, data:dict):
        self.id = data['id']
        self.name = data['name']
        self.cookie = data['cookie']
        self.boxes = data['boxes']
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
