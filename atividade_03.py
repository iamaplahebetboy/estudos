import random

# Lista de palavras para o jogo da forca
palavras = ['bambole', 'programa', 'intel', 'adedonha', 'monitor', 'nvidia', 'software']

# Função para escolher uma palavra aleatória
def escolher_palavra(palavras):
    return random.choice(palavras)

# Função para mostrar o estado atual da palavra ocultando letras não adivinhadas
def mostrar_palavra(palavra, letras_adivinhadas):
    resultado = ''
    for letra in palavra:
        if letra in letras_adivinhadas:
            resultado += letra
        else:
            resultado += '_'
    return resultado

# Função principal do jogo da forca
def jogo_da_forca():
    palavra = escolher_palavra(palavras)
    tentativas = 6
    letras_adivinhadas = []
    
    print("Bem-vindo ao Jogo da Forca!")
    
    while True:
        print("\nPalavra: " + mostrar_palavra(palavra, letras_adivinhadas))
        letra = input("Digite uma letra: ").lower()
        
        if letra in letras_adivinhadas:
            print("Você já adivinhou esta letra.")
        else:
            letras_adivinhadas.append(letra)
            if letra in palavra:
                print("Letra correta!")
                if mostrar_palavra(palavra, letras_adivinhadas) == palavra:
                    print("Parabéns, você venceu! A palavra é: " + palavra)
                    break
            else:
                tentativas -= 1
                print("Letra incorreta. Você tem {} tentativas restantes.".format(tentativas))
                if tentativas == 0:
                    print("Você perdeu! A palavra era: " + palavra)
                    break

# Executa o jogo
jogo_da_forca()
