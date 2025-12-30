from . import db

class Product(db.Model):
    __tablename__ = "products"

    product_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Product {self.product_id} - {self.name}>"
