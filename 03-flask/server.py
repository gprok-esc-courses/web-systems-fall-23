from flask import Flask, render_template, jsonify

app = Flask(__name__)

products = {
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
    if id in products:
        return render_template("product.html", id=id, name=products[id])
    else:
        return "Product not found"
    
@app.route("/api/products")
def api_products():
    return jsonify(products)

@app.route("/login")
def login():
    return render_template("login.html")


# Run the server: flask --app server --debug run