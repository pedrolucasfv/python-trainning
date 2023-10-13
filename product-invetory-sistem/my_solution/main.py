    
import product_functions

def contact_manager():
    product_list = [{'name': '', 'price': '', 'quantity': 0}]
    
    options = {
            '1': ['Adicionar Produto', product_functions.add_product],
            '2': ['Listar todos os produtos disponíveis', product_functions.list_products],
            '3': ['Buscar produtos por nome.', product_functions.search_product],
            '4': ['Atualizar informações de um produto.', product_functions.edit_product],
            '5': ['Remover produto do estoque.',product_functions.delete_product],
            '6': ['Mostrar produtos com baixo estoque.', product_functions.products_with_low_quantity],
            '0': ('Sair', None)
        }
       
    while True:
        
        print("\nMenu:")
        for key, value in options.items():
            print(f"{key} - {value[0]}")
            
        userOption = input("\n\nDigite o número da opção que você deseja: ")
        if(userOption == '0'):
            break
        elif userOption not in options:
            print('Opção inválida')
            continue
        else:
            message = options[userOption][1](product_list)
            print(message)
        
       
        
if __name__ == "__main__":
    print("Bem vindo ao Sistema de Estoque de Produtos")
    contact_manager()
    print('Volte sempre!')