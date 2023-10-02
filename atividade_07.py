import random

#Comando Randômico
numero_aleatorio = random.randint(1, 100)

#Comando inicial
print("Bem-vindo ao Jogo de Adivinhação!")
print("Tente adivinhar o número entre 1 e 100.")

tentativas = 0

#Introdução
while True:
    tentativa = int(input("Tentativa: "))
    tentativas += 1

    if tentativa < numero_aleatorio:
        print("Tente um número maior.")
    elif tentativa > numero_aleatorio:
        print("Tente um número menor.")
    else:
        print(f"Parabéns! Você acertou o número {numero_aleatorio} em {tentativas} tentativas.")
        break