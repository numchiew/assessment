from datetime import datetime
import json


class Product:

    def __init__(self, id, title, description, price, available_date, quantity, image_uri, is_special, category, tags,
                 created_time, modified_time):
        self.id = id,
        self.user_id = user_id
        self.title = title,
        self.description = description
        self.price = price
        self.available_date = available_date
        self.quantity = quantity
        self.image_uri = image_uri
        self.is_special = is_special
        self.category = category
        self.tags = tags
        self.created_time = datetime.strftime(created_time, '%d-%m-%Y')
        self.modified_time = datetime.strftime(modified_time, '%d-%m-%Y')


now = datetime.now()
tags = {'type': 'mug', 'sport': 'NBA'}
product = Product(1, 1, 'Basketball mug', 'Description', 150, now, 120, 's3://somewhere', False, 'MUG', json.dumps(tags), now,
                  now)
