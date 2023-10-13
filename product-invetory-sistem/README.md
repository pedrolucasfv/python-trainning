# Sistema de Estoque de Produtos em Python

Um sistema simples, porém eficiente, desenvolvido em Python para gerenciar um estoque de produtos.

## 📖 Descrição do Projeto

Este sistema permite ao usuário adicionar, listar, buscar, atualizar e remover produtos, bem como visualizar produtos com quantidade baixa no estoque. O sistema utiliza uma lista de dicionários para armazenar os produtos, cada um com seu nome, preço e quantidade.

## 🎓 Objetivo de Aprendizado

- **Modularização**: Aprender a dividir o código em módulos para melhor organização e manutenção.
- **Uso de Listas e Dicionários**: Praticar a utilização de listas e dicionários para armazenar e gerenciar dados.
- **Validação de Entrada**: Garantir que os dados inseridos pelo usuário sejam válidos.
- **Princípios DRY**: Evitar repetição de código, criando funções reutilizáveis.

## 🚀 Feedback Sobre a Solução Inicial

A implementação inicial do projeto estava no caminho certo, com funções claramente definidas e uma boa estrutura. No entanto, havia espaço para refatoração e otimização, principalmente em relação à organização do código e validações.

## 🎯 Versão Otimizada

### 🛠️ Melhorias Implementadas

- **Organização do Menu**: Refatorado o menu para tornar a adição ou remoção de novas opções mais simples.
- **Busca Otimizada**: Adicionada uma função de busca para evitar repetição de código.
- **Validações Aprimoradas**: Melhorada a validação de entradas e tratamento de erros.

## 📁 Estrutura do Projeto

- `main.py`: Contém a lógica principal do sistema e a interface do usuário.
- `product_functions.py`: Hospeda as funções relacionadas à gestão dos produtos.

## 📝 Sugestões e Pontos de Atenção

### Flexibilidade:
- **Quantidade Variável**: Atualmente, o limite para produtos com baixo estoque é fixo em 5. Para tornar esse valor flexível, pode-se considerar passar um parâmetro adicional à função ou usar uma variável global.

## ❓ Dúvidas

### Alterando a Quantidade Fixa na Função `products_with_low_quantity`

**Dúvida**: Como tornar a quantidade na função `products_with_low_quantity` variável, ao invés de fixa como 5?

**Resposta**:

1. **Passando um parâmetro adicional para a função**: Você pode passar um parâmetro adicional à função para definir o limiar de baixa quantidade. Confira o código de exemplo em [example_partial_threshold.py](./ia_solution/example_partial_threshold.py).

2. **Usando uma variável global no módulo**: Outra abordagem é usar uma variável global no módulo para definir o limiar de baixa quantidade. A função `products_with_low_quantity` se refere a essa variável global. Veja um exemplo detalhado em [example_global_threshold.py](./ia_solution/example_global_threshold.py).
