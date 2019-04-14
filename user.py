from userrole import UserRole


class User:
    def __init__(self, first_name, last_name, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.role = UserRole.LAZYBOB
        self.email = email
        self.created_at = 0
        self.location = location

    def update_role(self, role):
        self.role = UserRole(role)

    def get_cart(self):
        return self.cart

    def update_location(self, location):
        self.location = location

    def get_id(self):
        return self.id
