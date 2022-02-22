from flask import jsonify

from store_inventory.models import session, Product


PRODUCT_READY_TO_SHIP_STATE = 2


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


def update_product_state(id):
    product = session.query(Product).filter(Product.id == id).one_or_none()

    if product == None:
        return "<p>Not found</p>"

    product.product_state_id = PRODUCT_READY_TO_SHIP_STATE
    session.commit()

    return "<p>Product update</p>"


