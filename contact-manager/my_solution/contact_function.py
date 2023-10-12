

def add_contact(contact_list):
    name = input("Nome: ")
    phone = input("Telefone: ")
    email = input("Email: ")
    
    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }    
    contact_list.append(contact)
    return 'Contato adicionado com sucesso!'

def search_contact(contact_list):
    name = input("Nome: ")
    for contact in contact_list:
        if contact['name'] == name:
            print(f"Nome: {contact['name']}")
            print(f"Telefone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            return 'Contato encontrado!'
    
def list_contacts(contact_list):
    for contact in contact_list:
        print(f"Nome: {contact['name']}")
        print(f"Telefone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print('\n')
    return contact_list
def edit_contact(contact_list):
    print('Digite o nome do contato que deseja editar')
    name = input("Nome: ")
    for contact in contact_list:
        if contact['name'] == name:
            print(f"Nome: {contact['name']}")
            print(f"Telefone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            new_name = input("Novo nome: ")
            new_phone = input("Novo telefone: ")
            new_email = input("Novo email: ")
            contact['name'] = new_name
            contact['phone'] = new_phone
            contact['email'] = new_email
            return 'contato alterado com sucesso!'
        
def delete_contact(contact_list):
    print('Digite o nome do contato que deseja excluir')
    name = input("Nome: ")
    for contact in contact_list:
        if contact['name'] == name:
            contact_list.remove(contact)
            return 'Contato excluido com sucesso!'
    