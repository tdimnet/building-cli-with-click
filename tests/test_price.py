from store_inventory.utils.price import clean_price

def test_clean_price():
    price = clean_price('$4')
    assert 400 == price

