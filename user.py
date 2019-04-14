from userrole import UserRole


class User:
    def __init__(self, first_name, last_name, email, created_at, location):
        self.first_name = first_name
        self.last_name = last_name
        self.role = 0
        self.email = email
        self.created_at = created_at
        self.location = location

    def update_role(self, role):
        self.role = UserRole(role)

    def get_cart(self):
        return self.cart

    def update_location(self, location):
        self.location = location

    def get_id(self):
        return self.id
