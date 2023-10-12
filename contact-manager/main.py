    
import contact_function

def contact_manager():
    contact_list = [{'name': 'João', 'phone': '123456789', 'email': 'K5tK9@example.com'}]
    while True:
        print('1 - Adicionar Contato')
        print('2 - Buscar Contato')
        print('3 - Listar Contatos')
        print('4 - Editar Contato')
        print('5 - Excluir Contato')
        print('\n0 - Sair')
        userOption = input("\n\nDigite o número da opção que você deseja: ")
        
        options = {
            '1': contact_function.add_contact,
            '2': contact_function.search_contact,
            '3': contact_function.list_contacts,
            '4': contact_function.edit_contact,
            '5': contact_function.delete_contact
        }
        
        message = options[userOption](contact_list)
        
        print(message)
        if(userOption == '0'):
            break
        
if __name__ == "__main__":
    print("Bem vindo ao sistema de gerenciamento de contatos")
    contact_manager()