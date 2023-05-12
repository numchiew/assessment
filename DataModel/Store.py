from datetime import datetime
from StoreType import StoreType


class Store:

    def __init__(self, id, user_id, name, description, contact_information, store_type, created_time, modified_time):
        self.id = id
        self.user_id = user_id
        self.name = name,
        self.description = description
        self.contact_information = contact_information
        self.store_type = store_type.value
        self.created_time = datetime.strftime(created_time, '%d-%m-%Y')
        self.modified_time = datetime.strftime(modified_time, '%d-%m-%Y')


now = datetime.now()
store = Store(1, 1, 'Brikyl Shop', 'Description', 'address_information', StoreType.MICRO_STORE, now, now)
print(store.store_type)
