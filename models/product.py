from models import db

class Product(db.Model):
    __tablename__ = "products"   # ✅ ADD THIS

    product_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
