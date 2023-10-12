# Contact Manager

Um projeto de gerenciamento de contatos simples, porém robusto.

## 📖 Descrição do Projeto

Este sistema foi desenvolvido para gerenciar contatos de maneira eficiente. As funcionalidades incluem:

- **Adicionar Contato**: Permite ao usuário inserir um novo contato com nome, telefone e email.
- **Buscar Contato**: Realiza uma busca pelo nome e exibe as informações do contato encontrado.
- **Listar Contatos**: Mostra uma lista com todos os contatos salvos.
- **Editar Contato**: Permite alterar as informações de um contato existente.
- **Excluir Contato**: Remove um contato da lista.

## 🎓 Objetivo de Aprendizado

- **Estruturas de Dados**: Reforçar o entendimento sobre listas e dicionários em Python.
- **Modularização**: Praticar a divisão do código em módulos para melhor organização e manutenção.
- **Operações CRUD**: Aprender a implementar operações CRUD (Create, Read, Update, Delete) em uma estrutura de dados.
- **Interação com o Usuário**: Desenvolver habilidades em criar interfaces de texto intuitivas e amigáveis.


## 🚀 Feedback Sobre a Solução Inicial

O código original apresentou uma estruturação lógica clara, fazendo uso adequado de funções para modularizar cada operação. A estratégia de mapear as ações do usuário a funções específicas através de um dicionário demonstrou uma boa abordagem, tornando o código mais limpo e evitando condicionais extensas.

### 📝 Sugestões e Pontos de Atenção

1. **Validações**: 
   - É crucial garantir que o usuário não adicione contatos duplicados. 
   - Ao tentar editar ou excluir um contato, é importante verificar se o contato realmente existe.
   
2. **Refatoração e Reusabilidade**: 
   - A lógica de busca por nome foi repetida em várias funções. Isolar essa lógica em uma função separada pode melhorar a reusabilidade e manutenção do código.
   
3. **Feedback ao Usuário**: 
   - O usuário deve estar sempre informado sobre o que está acontecendo, seja uma operação bem-sucedida ou a ocorrência de um erro.

## 🎯 Versão Otimizada

Com base no feedback e análise do código original, desenvolveu-se uma versão otimizada. Esta nova versão busca melhorar a experiência do usuário e a manutenibilidade do código.

### 🛠️ Melhorias Implementadas

- **Função de Busca**: Criou-se uma função `find_contact_by_name` que centraliza a lógica de busca, evitando repetições e tornando o código mais DRY (Don't Repeat Yourself).
- **Mapeamento de Ações**: Refinou-se o dicionário `actions` para mapear as opções do usuário, tornando a adição de novas funcionalidades mais simples no futuro.
- **Validações Aprimoradas**: Introduziu-se verificações para garantir a consistência dos dados e evitar operações inválidas, como adicionar um contato já existente.
- **Listagem de Contatos**: Aprimorou-se a apresentação dos contatos, tornando a visualização mais clara e organizada para o usuário.

