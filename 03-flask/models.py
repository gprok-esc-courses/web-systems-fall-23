
class Product:
    def __init__(self, id, name, price) -> None:
        self.id = id
        self.name = name
        self.price = price

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price
        }