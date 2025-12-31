from flask import Blueprint, render_template
from models import Product, Location, ProductMovement

report_bp = Blueprint("report_bp", __name__)

@report_bp.route("/report")
def inventory_report():
    balances = {}

    movements = ProductMovement.query.all()

    # Calculate balances
    for m in movements:
        if m.from_location:
            key = (m.product_id, m.from_location)
            balances[key] = balances.get(key, 0) - m.qty

        if m.to_location:
            key = (m.product_id, m.to_location)
            balances[key] = balances.get(key, 0) + m.qty

    report_rows = []

    for (product_id, location_id), qty in balances.items():
        if qty == 0:
            continue

        product = Product.query.get(product_id)
        location = Location.query.get(location_id)

        report_rows.append({
            "product_name": product.name if product else product_id,
            "location_name": location.name if location else location_id,
            "qty": qty
        })

    # Sort for clean display
    report_rows.sort(key=lambda r: (r["product_name"], r["location_name"]))

    return render_template("report/inventory.html", report=report_rows)
