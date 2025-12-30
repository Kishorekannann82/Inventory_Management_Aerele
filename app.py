from flask import Flask, render_template
from config import Config
from models import db

from routes.product_routes import product_bp
from routes.location_routes import location_bp
from routes.movement_routes import movement_bp
from routes.report_routes import report_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(product_bp)
    app.register_blueprint(location_bp)
    app.register_blueprint(movement_bp)
    app.register_blueprint(report_bp)

    @app.route("/")
    def home():
        return render_template("home.html")

    # 🔴 THIS WAS MISSING
    return app


if __name__ == "__main__":
    app = create_app()

    # create tables (learning stage only)
    with app.app_context():
        db.create_all()

    app.run(debug=True)
