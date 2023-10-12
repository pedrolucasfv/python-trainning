import random

while True:
    
    randomNumber = random.randint(1, 10)
    
    for i in range(3):
        userNumber = int(input("Tente adivinhar o número sorteado: "))
        if userNumber == randomNumber:
            print("Parabéns, você acertou!")
            break
        elif userNumber > randomNumber:
            print("Mais baixo")
        else:
            print("Mais alto")
            
    print(f"Que pena, você perdeu, o número era {randomNumber}")
    
    userOption = input("Deseja jogar novamente? S/N: ")
    if(userOption == 'N'):
        print("Volte Sempre!")
        break
    elif(userOption == 'S'):
        print('Vamos lá!')
    else:
        print("Opção inválida")
        break
