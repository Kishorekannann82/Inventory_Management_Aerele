from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import models so Flask-Migrate & app can detect them
from .product import Product
from .location import Location
from .movement import ProductMovement
