from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Product

product_bp = Blueprint("product_bp", __name__)

# ----------------------------
# VIEW PRODUCTS
# ----------------------------
@product_bp.route("/products")
def list_products():
    products = Product.query.order_by(Product.product_id).all()
    return render_template("products/list.html", products=products)


# ----------------------------
# ADD PRODUCT
# ----------------------------
@product_bp.route("/products/add", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        product_id = request.form.get("product_id").strip()
        name = request.form.get("name").strip()
        description = request.form.get("description", "").strip()

        if not product_id or not name:
            flash("Product ID and Name are required.")
            return redirect(url_for("product_bp.add_product"))

        # check duplicate
        existing = Product.query.get(product_id)
        if existing:
            flash("Product ID already exists.")
            return redirect(url_for("product_bp.add_product"))

        product = Product(
            product_id=product_id,
            name=name,
            description=description
        )

        db.session.add(product)
        db.session.commit()

        flash("Product added successfully.")
        return redirect(url_for("product_bp.list_products"))

    return render_template("products/add.html")


# ----------------------------
# EDIT PRODUCT
# ----------------------------
@product_bp.route("/products/edit/<product_id>", methods=["GET", "POST"])
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)

    if request.method == "POST":
        name = request.form.get("name").strip()
        description = request.form.get("description", "").strip()

        if not name:
            flash("Product name is required.")
            return redirect(url_for("product_bp.edit_product", product_id=product_id))

        product.name = name
        product.description = description
        db.session.commit()

        flash("Product updated successfully.")
        return redirect(url_for("product_bp.list_products"))

    return render_template("products/edit.html", product=product)
