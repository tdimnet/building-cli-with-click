from flask import Flask, jsonify

from store_inventory.routes.hello import hello_world

from store_inventory.routes.products import (
    get_product,
    update_product_state
)


app = Flask(__name__)


app.add_url_rule("/", view_func=hello_world, methods=["GET"])

app.add_url_rule("/product/<id>", view_func=get_product, methods=["GET"])
app.add_url_rule("/product/<id>", view_func=update_product_state,
        methods=["PATCH"])

