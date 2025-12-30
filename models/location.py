from . import db

class Location(db.Model):
    __tablename__ = "locations"

    location_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Location {self.location_id} - {self.name}>"
