def clean_price(price_str):
    parse_to_float = float(price_str.replace("$", ""))
    return round(parse_to_float * 100)

