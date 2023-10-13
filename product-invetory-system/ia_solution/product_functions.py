def search_product_by_name(product_list, name):
    for product in product_list:
        if product['name'] == name:
            return product
    return None

def add_product(product_list):
    name = input("Nome: ")
    if search_product_by_name(product_list, name):
        return 'Produto já existe!'

    while True:
        try:
            price = float(input("Preço: "))
            break
        except ValueError:
            print("Informe um preço válido.")
    while True:
        try:
            quantity = int(input("Quantidade: "))
            break
        except ValueError:
            print("Informe uma quantidade válida.")

    product = {
        'name': name,
        'price': price,
        'quantity': quantity
    }    
    product_list.append(product)
    return 'Produto adicionado com sucesso!'

def list_products(product_list):
    for product in product_list:
        print(f"Nome: {product['name']}, Preço: {product['price']}, Quantidade: {product['quantity']}")
    return '\n\nLista de produtos no estoque.'

def search_product(product_list):
    name = input("Nome: ")
    product = search_product_by_name(product_list, name)
    if product:
        print(f"Nome: {product['name']}")
        print(f"Preço: {product['price']}")
        print(f"Quantidade: {product['quantity']}")
        return '\n\nProduto encontrado!'
    return 'Produto não encontrado.'

def edit_product(product_list):
    name = input("Nome do produto que deseja editar: ")
    product = search_product_by_name(product_list, name)
    if  product:
        product["name"] = input("Novo nome: ") or product["name"]
        while True:
            try:
                product["price"] = float(input("Novo preço: ") or product["price"])
                break
            except ValueError:
                print("Informe um preço válido.")
        while True:
            try:
                product["quantity"] = int(input("Nova quantidade: ") or product["quantity"])
                break
            except ValueError:
                print("Informe uma quantidade válida.")
        return "Produto alterado com sucesso!"
    return "Produto não encontrado."

def delete_product(product_list):
    name = input("Nome do produto que deseja excluir: ")
    product = search_product_by_name(product_list, name)
    if product:
        product_list.remove(product)
        return 'Produto excluído com sucesso!'

def products_with_low_quantity(product_list):
    low_stock_products = [product for product in product_list if product['quantity'] < 5]
    for product in low_stock_products:
        print(f"Nome: {product['name']}, Preço: {product['price']}, Quantidade: {product['quantity']}")
    if low_stock_products:
        return '\n\nLista de produtos com baixo estoque.'
    return 'Nenhum produto com baixo estoque.'
