from flask import Blueprint, request, render_template, redirect, url_for
from models import db, Product

product_bp = Blueprint("product", __name__)

# -------------------------
# View Products
# -------------------------
@product_bp.route("/products", methods=["GET"])
def list_products():
    products = Product.query.all()
    return render_template("products/list.html", products=products)


# -------------------------
# Add Product
# -------------------------
@product_bp.route("/products/add", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        product_id = request.form.get("product_id")
        name = request.form.get("name")

        if product_id and name:
            product = Product(product_id=product_id, name=name)
            db.session.add(product)
            db.session.commit()

            return redirect(url_for("product.list_products"))

    return render_template("products/add.html")
