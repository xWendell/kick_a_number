import random

# Numero aleatorio de 1 a 100
num_aleatorio = random.randint(1, 100)

# Inicializacao
tentativas = 0
maximo_de_tentativas = 8

print('Bem-vindo ao jogo de adivinhação!')
print(f'Você tem {maximo_de_tentativas} tentativas.')

while tentativas < maximo_de_tentativas:
    try:
        num_do_usuario = int(input('Chute um numero de 1-100: '))
        if num_do_usuario < 1 or num_do_usuario > 100:
            print('Chute um número entre 1 e 100.')
            continue

        tentativas += 1
        tentativas_restantes = maximo_de_tentativas - tentativas

        if num_do_usuario == num_aleatorio:
            print(f'\nParabéns, você acertou em {tentativas} tentativas!')
            break
        elif num_do_usuario < num_aleatorio:
            print(f'Tentativas restantes: {tentativas_restantes}')
            print('Chute um número mais alto!\n')
        else:
            print(f"Tentativas restantes: {tentativas_restantes}")
            print('Chute um número mais baixo!\n')
    except ValueError:
        print('Entrada inválida. Digite apenas números inteiros.')

if tentativas == maximo_de_tentativas and num_do_usuario != num_aleatorio:
    print('\nVocê perdeu!')
    print(f'O número correto era {num_aleatorio}')
