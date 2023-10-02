import os
#Introdução do comando
def mostrar_filmes_disponiveis(filmes):
    print("Filmes Disponíveis:")
    for i, filme in enumerate(filmes, start=1):
        print(f"{i}. {filme['nome']} ({filme['horario']}) - {filme['vagas']} vagas disponíveis")

def fazer_reserva(filmes, filme_index):
    if 1 <= filme_index <= len(filmes):
        filme = filmes[filme_index - 1]
        if filme['vagas'] > 0:
            filme['vagas'] -= 1
            return f"Reserva feita para {filme['nome']} ({filme['horario']})."
        else:
            return "Desculpe, não há vagas disponíveis para este filme."
    else:
        return "Filme selecionado não existe."

arquivo_reservas = 'reservas.txt'

filmes_disponiveis = [
    {'nome': 'Filme A', 'horario': '10:00', 'vagas': 5},
    {'nome': 'Filme B', 'horario': '14:30', 'vagas': 10},
    {'nome': 'Filme C', 'horario': '18:15', 'vagas': 7}
]

reservas = []
if os.path.exists(arquivo_reservas):
    with open(arquivo_reservas, 'r') as f:
        reservas = f.read().splitlines()

while True:
    print("\nSistema de Reservas de Cinema")
    mostrar_filmes_disponiveis(filmes_disponiveis)
    print("0. Sair")

    escolha = input("Escolha um filme (ou 0 para sair): ")

    if escolha == '0':
        break
    else:
        try:
            escolha = int(escolha)
            if 1 <= escolha <= len(filmes_disponiveis):
                filme_index = escolha
                mensagem = fazer_reserva(filmes_disponiveis, filme_index)
                if "Desculpe" in mensagem:
                    print(mensagem)
                else:
                    print(mensagem)
                    reservas.append(f"Reserva: {mensagem}")
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Opção inválida. Tente novamente.")

# Salvar as reservas no arquivo
with open(arquivo_reservas, 'w') as f:
    f.write('\n'.join(reservas))
