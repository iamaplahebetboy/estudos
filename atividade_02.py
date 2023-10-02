
import csv
import os

def criar_agenda(arquivo):
    with open(arquivo, 'w', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow(['Nome', 'Telefone'])

def adicionar_contato(arquivo, nome, telefone):
    with open(arquivo, 'a', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow([nome, telefone])

def listar_contatos(arquivo):
    with open(arquivo, 'r') as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        for row in reader:
            print(f'Nome: {row[0]}, Telefone: {row[1]}')

def buscar_contato(arquivo, nome):
    with open(arquivo, 'r') as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        encontrado = False
        for row in reader:
            if nome.lower() in row[0].lower():
                print(f'Nome: {row[0]}, Telefone: {row[1]}')
                encontrado = True
        if not encontrado:
            print('Contato não encontrado.')

def remover_contato(arquivo, nome):
    linhas = []
    with open(arquivo, 'r') as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        for row in reader:
            if nome.lower() not in row[0].lower():
                linhas.append(row)
    
    with open(arquivo, 'w', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        for row in linhas:
            writer.writerow(row)

# Nome do arquivo CSV para armazenar os contatos
arquivo_agenda = 'agenda.csv'

if not os.path.isfile(arquivo_agenda):
    criar_agenda(arquivo_agenda)
#opções
while True:
    print("\nAgenda de Contatos")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Buscar Contato")
    print("4. Remover Contato")
    print("5. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    #escolhas
    if escolha == '1':
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        adicionar_contato(arquivo_agenda, nome, telefone)
        print("Contato adicionado com sucesso.")
    elif escolha == '2':
        print("\nLista de Contatos:")
        listar_contatos(arquivo_agenda)
    elif escolha == '3':
        nome = input("Digite o nome do contato que deseja buscar: ")
        buscar_contato(arquivo_agenda, nome)
    elif escolha == '4':
        nome = input("Digite o nome do contato que deseja remover: ")
        remover_contato(arquivo_agenda, nome)
        print("Contato removido com sucesso.")
    elif escolha == '5':
        print("Saindo da Agenda de Contatos. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
