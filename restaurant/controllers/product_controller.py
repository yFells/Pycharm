from flask import Flask, request,render_template,redirect,url_for, Blueprint
produtos = []
ingredientes = []
registered = {}

product = Blueprint("product", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

@product.route("/")
def products_index():
    return render_template("/product/product_index.html")

@product.route("/regis", methods=['POST','GET'])
def products_regis():
    return render_template("/product/produto_regis.html")

@product.route("/registrar", methods=['POST','GET'])
def produto_registrar():
    if request.method == 'POST':
        name = request.form['product_name']
        descricao = request.form['txt_descricao']
        valor = request.form['num_valor']
        quantidade = request.form['num_qtd']
        global registered
        id = len(registered) + 1
        registered[id] = {'name':name, 'descricao': descricao, 'valor':valor,'quantidade':quantidade}
        #return registered
        return redirect("listar_produtos")

    #produtos = ["Pão quente","Pão com queijo e presunto na chapa", 5, 45]



@product.route("/ingredientes", methods=['POST','GET'])
def produto_ingredientes():
    return render_template("/product/product_ingre.html", produto_array=registered)

@product.route("/regis_ingredientes", methods=['POST','GET'])
def produto_regis_ingredientes():
    if request.method == 'POST':
        txtProduto = request.form['txtProduto']
        nomeIngrediente = request.form['txtName']
        quantidade = request.form['txtQtd']
        global registered
        #numero diferente conforme meu valor da pagina
        #id = len(registered) + 1
        registered[txtProduto] = {'nomeIngrediente':nomeIngrediente,'QtdIngrediente':quantidade}
        # return registered
        return redirect("listar_produtos")

@product.route("/listar_produtos", methods=['POST','GET'])
def produto_listar():
    #produtos = ["Pão quente", "Pão com queijo e presunto na chapa", 5, 45]
    #if request.method == 'POST':
        #nome_produto = request.form['product_name']
    return render_template("/product/product_listar.html", produto_array=registered)
