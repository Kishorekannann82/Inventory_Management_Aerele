from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Product, Location, ProductMovement

movement_bp = Blueprint("movement_bp", __name__)

# ----------------------------
# VIEW MOVEMENTS
# ----------------------------
@movement_bp.route("/movements")
def list_movements():
    movements = ProductMovement.query.order_by(ProductMovement.timestamp.desc()).all()
    return render_template("movements/list.html", movements=movements)


# ----------------------------
# ADD MOVEMENT
# ----------------------------
@movement_bp.route("/movements/add", methods=["GET", "POST"])
def add_movement():
    products = Product.query.all()
    locations = Location.query.all()

    if request.method == "POST":
        movement_id = request.form.get("movement_id").strip()
        product_id = request.form.get("product_id")
        from_location = request.form.get("from_location") or None
        to_location = request.form.get("to_location") or None
        qty = request.form.get("qty")

        # validations
        if not movement_id or not product_id or not qty:
            flash("Movement ID, Product and Quantity are required.")
            return redirect(url_for("movement_bp.add_movement"))

        if not from_location and not to_location:
            flash("Either From Location or To Location must be selected.")
            return redirect(url_for("movement_bp.add_movement"))

        qty = int(qty)
        if qty <= 0:
            flash("Quantity must be greater than zero.")
            return redirect(url_for("movement_bp.add_movement"))

        movement = ProductMovement(
            movement_id=movement_id,
            product_id=product_id,
            from_location=from_location,
            to_location=to_location,
            qty=qty
        )

        db.session.add(movement)
        db.session.commit()

        flash("Product movement recorded.")
        return redirect(url_for("movement_bp.list_movements"))

    return render_template(
        "movements/add.html",
        products=products,
        locations=locations
    )


# ----------------------------
# EDIT MOVEMENT
# ----------------------------
@movement_bp.route("/movements/edit/<movement_id>", methods=["GET", "POST"])
def edit_movement(movement_id):
    movement = ProductMovement.query.get_or_404(movement_id)
    products = Product.query.all()
    locations = Location.query.all()

    if request.method == "POST":
        product_id = request.form.get("product_id")
        from_location = request.form.get("from_location") or None
        to_location = request.form.get("to_location") or None
        qty = int(request.form.get("qty"))

        if not from_location and not to_location:
            flash("Either From or To location must be selected.")
            return redirect(url_for("movement_bp.edit_movement", movement_id=movement_id))

        movement.product_id = product_id
        movement.from_location = from_location
        movement.to_location = to_location
        movement.qty = qty

        db.session.commit()
        flash("Movement updated successfully.")
        return redirect(url_for("movement_bp.list_movements"))

    return render_template(
        "movements/edit.html",
        movement=movement,
        products=products,
        locations=locations
    )
