from flask import Blueprint, request, render_template, redirect, url_for
from models import db, ProductMovement

movement_bp = Blueprint("movement", __name__)

# -------------------------
# View Movements
# -------------------------
@movement_bp.route("/movements", methods=["GET"])
def list_movements():
    movements = ProductMovement.query.order_by(ProductMovement.timestamp.desc()).all()
    return render_template("movements/list.html", movements=movements)


# -------------------------
# Add Movement
# -------------------------
@movement_bp.route("/movements/add", methods=["GET", "POST"])
def add_movement():
    if request.method == "POST":
        movement_id = request.form.get("movement_id")
        product_id = request.form.get("product_id")
        from_location = request.form.get("from_location") or None
        to_location = request.form.get("to_location") or None
        qty = request.form.get("qty")

        if movement_id and product_id and qty and (from_location or to_location):
            movement = ProductMovement(
                movement_id=movement_id,
                product_id=product_id,
                from_location=from_location,
                to_location=to_location,
                qty=int(qty)
            )
            db.session.add(movement)
            db.session.commit()

            return redirect(url_for("movement.list_movements"))

    return render_template("movements/add.html")
