from status import ItemStatus


class Item:
    def __init__(self, name, store, price, size, description, created_by):
        self.name = name
        self.store = store
        self.price = price
        self.size = size
        self.description = description
        self.status = ItemStatus.CART
        self.created_by = created_by
        self.shopper_id = None

    def update_status(self, status):
        self.status = status

    def update_shopper(self, shopper_id):
        self.shopper_id = shopper_id
