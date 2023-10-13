# Simple Python Calculator

Uma calculadora intuitiva construída em Python que permite ao usuário realizar operações básicas de matemática.

## 📖 Descrição do Projeto

Esta calculadora suporta as operações de adição, subtração, multiplicação e divisão. Ela foi projetada para aceitar a expressão matemática como uma única string (por exemplo, `5+3`) e, em seguida, calcular e exibir o resultado.

## 🎓 Objetivo de Aprendizado

- **Modularização**: Aprender a dividir o código em módulos distintos para melhor organização e manutenção.
- **Uso de Dicionários**: Praticar a utilização de dicionários para mapear operações e funções.
- **Validação de Entrada**: Trabalhar com validações para garantir a correta execução do programa.
- **Princípios DRY**: Evitar repetição de código através da criação de funções reutilizáveis.

## 🚀 Feedback Sobre a Solução Inicial

O projeto inicial estava bem estruturado, com uma abordagem direta para identificar e realizar operações matemáticas. No entanto, faltava modularização e algumas melhorias na organização do código.

## 📝 Sugestões e Pontos de Atenção

- **Validações**: Garanta que a entrada do usuário seja correta e que erros, como divisão por zero, sejam tratados adequadamente.
- **Refatoração**: Considere a utilização de funções adicionais ou classes para modularizar ainda mais o código e torná-lo mais legível.

## 🎯 Versão Otimizada

Com base no feedback e análise, desenvolveu-se uma versão otimizada:

### 🛠️ Melhorias Implementadas

- **Divisão em Dois Arquivos**: O código foi dividido em dois arquivos - um para a lógica principal (`main.py`) e outro para as operações matemáticas (`math_operations.py`).
- **Uso de Dicionários**: Mapeamento dos operadores às suas respectivas operações, permitindo uma fácil expansão no futuro.
- **Validações Aprimoradas**: Adicionada verificação para divisão por zero e validação da entrada do usuário.

## 📁 Estrutura do Projeto

- `main.py`: Contém a lógica principal da calculadora e a interface do usuário.
- `math_operations.py`: Hospeda funções para cada operação matemática.

