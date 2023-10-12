# main.py
import contact_functions as cf

def contact_manager():
    contact_list = [{'name': 'João', 'phone': '123456789', 'email': 'K5tK9@example.com'}]
    
    actions = {
        '1': ('Adicionar Contato', cf.add_contact),
        '2': ('Buscar Contato', cf.search_contact),
        '3': ('Listar Contatos', cf.list_contacts),
        '4': ('Editar Contato', cf.edit_contact),
        '5': ('Excluir Contato', cf.delete_contact),
        '0': ('Sair', None)
    }

    while True:
        print("\nMenu:")
        for key, value in actions.items():
            print(f"{key} - {value[0]}")
        
        user_option = input("\nDigite o número da opção que você deseja: ")
        
        if user_option == '0':
            break
        
        if user_option not in actions:
            print("Opção inválida!")
            continue
        
        result_message = actions[user_option][1](contact_list)
        if result_message:
            print(result_message)
        
if __name__ == "__main__":
    print("Bem-vindo ao sistema de gerenciamento de contatos!")
    contact_manager()
    print("Volte sempre!")
