from flask import Blueprint, render_template
produtos = []
ingredientes = []


product = Blueprint("product", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

@product.route("/")
def products_index():
    return render_template("/product/product_index.html")

@product.route("/registrar")
def produto_regis():
    #if request.method == 'POST':
        #nome_produto = request.form['product_name']
    produtos = ["Pão quente","Pão com queijo e presunto na chapa", 5, 45]
    return render_template("/product/produto_regis.html", produto_array=produtos)


@product.route("/ingredientes")
def produto_ingredientes():
    return render_template("/product/product_ingre.html", produto_array=ingredientes)

@product.route("/listar_produtos")
def produto_listar():
    produtos = ["Pão quente", "Pão com queijo e presunto na chapa", 5, 45]
    #if request.method == 'POST':
        #nome_produto = request.form['product_name']
    return render_template("/product/product_listar.html", produto_array=produtos)
