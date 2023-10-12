# Random Number Guessing Game

Um jogo interativo onde o jogador tenta adivinhar um número aleatório gerado pelo sistema.

## 📖 Descrição do Projeto

Neste jogo, o sistema gera um número aleatório entre 1 e 10. O jogador tem três tentativas para adivinhar qual é esse número. A cada tentativa, o sistema fornece uma dica se o número escolhido pelo jogador é maior ou menor que o número gerado.

## 🎓 Objetivo de Aprendizado

- **Uso de Bibliotecas**: Praticar a importação e utilização de bibliotecas externas, neste caso, a `random`.
- **Controle de Fluxo**: Reforçar o entendimento sobre loops e condicionais.
- **Interação com o Usuário**: Melhorar as habilidades de obter e processar a entrada do usuário de maneira eficiente.
- **Feedback Instantâneo**: Aprender a fornecer feedback imediato ao usuário com base em suas ações.

## 🚀 Feedback Sobre a Solução Inicial

O código original fazia uso de estruturas condicionais para identificar e informar ao jogador se o número escolhido estava correto, se era maior ou menor que o número gerado. Além disso, utilizava um loop para permitir ao jogador continuar jogando por quantas vezes desejasse.

### 📝 Sugestões e Pontos de Atenção

1. **Validações**:
   - É importante garantir que o jogador insira apenas números válidos e dentro do intervalo permitido.
   
2. **Refatoração**:
   - O uso de funções pode modularizar o código, tornando-o mais legível e mantendo o código DRY (Don't Repeat Yourself).

## 🎯 Versão Otimizada

Baseado no feedback e análise do código original, desenvolveu-se uma versão otimizada. Esta nova versão busca melhorar a experiência do usuário e a manutenibilidade do código.

### 🛠️ Melhorias Implementadas

- **Uso de Dicionários**: Para mapear as operações de verificação (maior, menor ou igual) e otimizar a lógica de comparação.
- **Funções Separadas**: Modularizou-se o código em funções distintas para cada operação, como `generate_random_number` e `get_user_guess`.
- **Feedback Aprimorado ao Usuário**: Melhoria nas mensagens de feedback ao jogador, tornando a interação mais amigável e informativa.

