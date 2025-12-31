from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Location

location_bp = Blueprint("location_bp", __name__)

# VIEW LOCATIONS
@location_bp.route("/locations")
def list_locations():
    locations = Location.query.order_by(Location.location_id).all()
    return render_template("locations/list.html", locations=locations)


# ADD LOCATION

@location_bp.route("/locations/add", methods=["GET", "POST"])
def add_location():
    if request.method == "POST":
        location_id = request.form.get("location_id").strip()
        name = request.form.get("name").strip()

        if not location_id or not name:
            flash("Location ID and Name are required.")
            return redirect(url_for("location_bp.add_location"))

        existing = Location.query.get(location_id)
        if existing:
            flash("Location ID already exists.")
            return redirect(url_for("location_bp.add_location"))

        location = Location(
            location_id=location_id,
            name=name
        )

        db.session.add(location)
        db.session.commit()

        flash("Location added successfully.")
        return redirect(url_for("location_bp.list_locations"))

    return render_template("locations/add.html")



# EDIT LOCATION

@location_bp.route("/locations/edit/<location_id>", methods=["GET", "POST"])
def edit_location(location_id):
    location = Location.query.get_or_404(location_id)

    if request.method == "POST":
        name = request.form.get("name").strip()

        if not name:
            flash("Location name is required.")
            return redirect(url_for("location_bp.edit_location", location_id=location_id))

        location.name = name
        db.session.commit()

        flash("Location updated successfully.")
        return redirect(url_for("location_bp.list_locations"))

    return render_template("locations/edit.html", location=location)
