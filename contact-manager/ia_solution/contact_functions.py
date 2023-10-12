# contact_functions.py
def find_contact_by_name(contact_list, name):
    for contact in contact_list:
        if contact["name"].lower() == name.lower():
            return contact
    return None

def add_contact(contact_list):
    name = input("Nome: ")
    if find_contact_by_name(contact_list, name):
        return "Contato já existe!"

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
    name = input("Nome do contato que deseja buscar: ")
    contact = find_contact_by_name(contact_list, name)
    if contact:
        print(f"Nome: {contact['name']}")
        print(f"Telefone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        return "Contato encontrado!"
    return "Contato não encontrado."

def list_contacts(contact_list):
    for contact in contact_list:
        print(f"Nome: {contact['name']}, Telefone: {contact['phone']}, Email: {contact['email']}")

def edit_contact(contact_list):
    name = input("Nome do contato que deseja editar: ")
    contact = find_contact_by_name(contact_list, name)
    if contact:
        contact["name"] = input("Novo nome: ") or contact["name"]
        contact["phone"] = input("Novo telefone: ") or contact["phone"]
        contact["email"] = input("Novo email: ") or contact["email"]
        return "Contato alterado com sucesso!"
    return "Contato não encontrado."

def delete_contact(contact_list):
    name = input("Nome do contato que deseja excluir: ")
    contact = find_contact_by_name(contact_list, name)
    if contact:
        contact_list.remove(contact)
        return "Contato excluído com sucesso!"
    return "Contato não encontrado."
