from . import db
from datetime import datetime

class ProductMovement(db.Model):
    __tablename__ = "product_movements"

    movement_id = db.Column(db.String, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    product_id = db.Column(
        db.String,
        db.ForeignKey("products.product_id"),
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

    def __repr__(self):
        return (
            f"<Movement {self.movement_id} | "
            f"Product {self.product_id} | Qty {self.qty}>"
        )
