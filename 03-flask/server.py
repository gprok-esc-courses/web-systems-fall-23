from flask import Flask, render_template, jsonify, request, redirect
import database

app = Flask(__name__)

# Check if DB exists and if not create it
database.create_db()

products_list = {
    '1': "Mouse", 
    '2': "Keyboard",
    '3': "Monitor"
}

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/product/<id>")
def product(id):
    product = database.get_product(id)
    if product:
        return render_template("product.html", id=product.id, name=product.name, price=product.price)
    else:
        return jsonify({'Error': 'Product not found'})
    
@app.route("/products")
def products():
    products = database.get_all_products()
    return render_template("products.html", products=products)
    
@app.route("/api/products")
def api_products():
    products = database.get_all_products()
    products_json = []
    for product in products:
        products_json.append(product.serialize())
    return jsonify({'products': products_json})


@app.route("/add/product")
def add_product():
    return render_template("add_product_form.html")

@app.route("/add/product", methods=['POST'])
def do_add_product():
    data = request.form
    print(data['name'], data['price'])
    database.add_product(data['name'], data['price'])
    return redirect('/products')
    


@app.route("/login")
def login():
    return render_template("login.html")


# Run the server: flask --app server --debug run