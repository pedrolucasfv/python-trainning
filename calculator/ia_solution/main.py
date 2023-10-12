import math_functions

def calculator():
    operations = {
        '+': math_functions.add,
        '-': math_functions.subtract,
        '*': math_functions.multiply,
        '/': math_functions.divide
    }

    while True:
        expression = input("Digite sua operação (ex: 5+3) ou 'exit' para sair: ")
        
        if expression.lower() == 'exit':
            print("Obrigado por usar a calculadora! Até mais!")
            break
        
        for operator in operations:
            if operator in expression:
                x, y = map(int, expression.split(operator))
                result = operations[operator](x, y)
                print(f"Resultado: {result}")
                break
        else:
            print("Operação inválida.")

if __name__ == "__main__":
    print("Bem-vindo à calculadora!")
    calculator()
