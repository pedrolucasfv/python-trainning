import random

def generate_random_number():
    """Gera um número aleatório entre 1 e 10."""
    return random.randint(1, 10)

def get_user_guess():
    """Solicita ao usuário um palpite e garante que é um número válido entre 1 e 10."""
    while True:
        try:
            guess = int(input("Tente adivinhar o número sorteado entre 1 e 10: "))
            if 1 <= guess <= 10:
                return guess
            else:
                print("Por favor, insira um número entre 1 e 10.")
        except ValueError:
            print("Isso não é um número válido. Tente novamente.")

def main_game_loop():
    print("Bem-vindo ao jogo de adivinhação!")
    while True:
        random_number = generate_random_number()
        for _ in range(3):
            user_guess = get_user_guess()
            if user_guess == random_number:
                print("Parabéns, você acertou!")
                break
            elif user_guess < random_number:
                print("Tente um número maior.")
            else:
                print("Tente um número menor.")
        else:
            print(f"Que pena, você não acertou. O número era {random_number}.")

        play_again = input("Deseja jogar novamente? (S/N): ").lower()
        if play_again != 's':
            print("Obrigado por jogar! Até mais!")
            break

if __name__ == "__main__":
    main_game_loop()
