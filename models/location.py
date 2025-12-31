from models import db

class Location(db.Model):
    __tablename__ = "locations"  # ✅ ADD THIS

    location_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
