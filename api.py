from flask import Flask, jsonify

from store_inventory.models import session, Product

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World</p>"


@app.route("/product/<id>")
def get_product(id):
    product = session.query(Product).filter(Product.id == id).one_or_none()

    if product == None:
        return "<p>Not found</p>"

    data = {
        "id": product.id,
        "name": product.name,
        "product_state": product.product_state_id
    }

    return jsonify(data)

