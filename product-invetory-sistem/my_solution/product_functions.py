def search_product_by_name(product_list, name):
    for product in product_list:
        if product['name'] == name:
            return product
    return None

def add_product(product_list):
    name = input("Nome: ")
    
    if search_product_by_name(product_list, name):
        return 'Contato já existe!'
    
    price = input("preço: ")
    quantity = input("quantidade: ")
    
    product = {
        'name': name,
        'price': price,
        'quantity': quantity
    }    
    product_list.append(product)
    return 'Produto adicionado com sucesso!'

def list_products(product_list):
    for product in product_list:
       print(f"Nome: {product['name']}, Telefone: {product['price']}, Email: {product['quantity']}")
    return '\n\nLista de produtos no estoque.'

def search_product(product_list):
    name = input("Nome: ")
    
    product = search_product_by_name(product_list, name)
    
    if product:
        print(f"Nome: {product['name']}")
        print(f"Telefone: {product['phone']}")
        print(f"Email: {product['email']}")
        return '\n\nContato encontrado!'
    return 'Contato não encontrado.'
    

def edit_product(product_list):
    name = input("Nome do produto que deseja editar: ")
    product = search_product_by_name(product_list, name)
    if  product:
        product["name"] = input("Novo nome: ") or product["name"]
        product["price"] = input("Novo preço: ") or product["price"]
        product["quantity"] = input("Nova quantidade: ") or product["quantity"]
        return "Produto alterado com sucesso!"
    return "Produto não encontrado."
        
def delete_product(product_list):
    print('Digite o nome do produto que deseja excluir')
    name = input("Nome: ")
    product = search_product_by_name(product_list, name)
    if product:
        product_list.remove(product)
        return 'Produto excluído com sucesso!'
    
def products_with_low_quantity(product_list):
    for product in product_list:
        if product['quantity'] < 5:
             print(f"Nome: {product['name']}, Telefone: {product['price']}, Email: {product['quantity']}")
             return '\n~Lista de produtos com baixo estoque'
    return 'Nenhum produto com baixo estoque'