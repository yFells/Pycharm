from flask import Blueprint, render_template
produtos = []
ingredientes = []


product = Blueprint("product", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

@product.route("/")
def products_index():
    return render_template("/product/product_index.html")

@product.route("/regis")
def produto_regis():
    return render_template("/product/produto_regis.html", produto_array=produtos)

@product.route("/ingredientes")
def produto_ingredientes():
    return render_template("/product/product_ingre.html", produto_array=ingredientes)

