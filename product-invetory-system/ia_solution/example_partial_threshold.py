# example_partial_threshold.py
from functools import partial

def products_with_low_quantity(product_list, threshold):
    for product in product_list:
        if product['quantity'] < threshold:
            print(f"Nome: {product['name']}, Preço: {product['price']}, Quantidade: {product['quantity']}")

# Demonstração:
# custom_threshold_function = partial(products_with_low_quantity, threshold=10)
# custom_threshold_function(product_list)
