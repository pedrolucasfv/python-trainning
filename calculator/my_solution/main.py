import math_functions

def calculator():
    while True:
        option = input("Digite a operação desejada: ").replace(' ', '')
        
        if('+' in option):
            numbers = option.split('+')
            print(math_functions.soma(int(numbers[0]), int(numbers[1])))
        elif('-' in option):
            numbers = option.split('-')
            print(math_functions.subtracao(int(numbers[0]), int(numbers[1])))
        elif('*' in option):
            numbers = option.split('*')
            print(math_functions.multiplicacao(int(numbers[0]), int(numbers[1])))
         
        elif('/' in option):
            numbers = option.split('/')
            print(math_functions.divisao(int(numbers[0]), int(numbers[1])))
        else:
            print('operação inválida')
        
        
        userOption = input("Deseja executar novamente? S/N: ").lower()
        if(userOption == 'n'):
            print("Volte Sempre!")
            return
        elif(userOption == 's'):
            print('Vamos la!')


if __name__ == "__main__":
    print("Bem vindo a calculadora")
    calculator()