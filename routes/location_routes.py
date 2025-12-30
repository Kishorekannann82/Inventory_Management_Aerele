from flask import Blueprint, request, render_template, redirect, url_for
from models import db, Location

location_bp = Blueprint("location", __name__)

# -------------------------
# View Locations
# -------------------------
@location_bp.route("/locations", methods=["GET"])
def list_locations():
    locations = Location.query.all()
    return render_template("locations/list.html", locations=locations)


# -------------------------
# Add Location
# -------------------------
@location_bp.route("/locations/add", methods=["GET", "POST"])
def add_location():
    if request.method == "POST":
        location_id = request.form.get("location_id")
        name = request.form.get("name")

        if location_id and name:
            location = Location(location_id=location_id, name=name)
            db.session.add(location)
            db.session.commit()

            return redirect(url_for("location.list_locations"))

    return render_template("locations/add.html")
