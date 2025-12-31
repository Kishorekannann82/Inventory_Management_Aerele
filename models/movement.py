from models import db
from datetime import datetime

class ProductMovement(db.Model):
    __tablename__ = "product_movements"  # ✅ ADD THIS

    movement_id = db.Column(db.String, primary_key=True)

    product_id = db.Column(
        db.String,
        db.ForeignKey("products.product_id"),  # ✅ NOW MATCHES
        nullable=False
    )

    from_location = db.Column(
        db.String,
        db.ForeignKey("locations.location_id"),
        nullable=True
    )

    to_location = db.Column(
        db.String,
        db.ForeignKey("locations.location_id"),
        nullable=True
    )

    qty = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
