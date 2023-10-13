# example_global_threshold.py

LOW_QUANTITY_THRESHOLD = 5

def products_with_low_quantity(product_list):
    for product in product_list:
        if product['quantity'] < LOW_QUANTITY_THRESHOLD:
            print(f"Nome: {product['name']}, Preço: {product['price']}, Quantidade: {product['quantity']}")

def set_low_quantity_threshold(new_threshold):
    global LOW_QUANTITY_THRESHOLD
    LOW_QUANTITY_THRESHOLD = new_threshold

# Demonstração:
# set_low_quantity_threshold(10)
# products_with_low_quantity(product_list)
