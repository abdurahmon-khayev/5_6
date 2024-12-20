from collections import namedtuple


class Product(namedtuple('Product', ['name', 'price'])):
    __slots__ = ()

    def is_expensive(self, threshold):
        return self.price > threshold


class User(namedtuple('User', ['username', 'email'])):
    __slots__ = ()

    def is_email_valid(self):
        return '@' in self.email


product = Product(name="Laptop", price=1500)
user = User(username="johndoe", email="johndoe@example.com")

print(f"Mahsulot qimmatmi? {product.is_expensive(1000)}")
print(f"Email validmi? {user.is_email_valid()}")
