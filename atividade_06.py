
import json
import os


def carregar_tarefas(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            tarefas = json.load(f)
    else:
        tarefas = []
    return tarefas


def salvar_tarefas(arquivo, tarefas):
    with open(arquivo, 'w') as f:
        json.dump(tarefas, f)


def adicionar_tarefa(tarefas, descricao):
    tarefa = {'descricao': descricao, 'concluida': False}
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

# Função para listar tarefas
def listar_tarefas(tarefas):
    for idx, tarefa in enumerate(tarefas, start=1):
        status = "Concluída" if tarefa['concluida'] else "Pendente"
        print(f"{idx}. [{status}] {tarefa['descricao']}")

# Função para marcar tarefa como concluída
def marcar_concluida(tarefas, indice):
    if 1 <= indice <= len(tarefas):
        tarefa = tarefas[indice - 1]
        tarefa['concluida'] = True
        print("Tarefa marcada como concluída.")
    else:
        print("Índice inválido.")

# Função para remover tarefa
def remover_tarefa(tarefas, indice):
    if 1 <= indice <= len(tarefas):
        tarefa_removida = tarefas.pop(indice - 1)
        print(f"Tarefa removida: {tarefa_removida['descricao']}")
    else:
        print("Índice inválido.")

arquivo_tarefas = 'tarefas.json'

tarefas = carregar_tarefas(arquivo_tarefas)

while True:
    print("\nAplicativo de Gerenciamento de Tarefas")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Remover Tarefa")
    print("5. Sair")

#Lista de escolhas 
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        descricao = input("Digite a descrição da tarefa: ")
        adicionar_tarefa(tarefas, descricao)
        salvar_tarefas(arquivo_tarefas, tarefas)
    elif escolha == '2':
        print("\nLista de Tarefas:")
        listar_tarefas(tarefas)
    elif escolha == '3':
        listar_tarefas(tarefas)
        indice = int(input("Digite o índice da tarefa a ser marcada como concluída: "))
        marcar_concluida(tarefas, indice)
        salvar_tarefas(arquivo_tarefas, tarefas)
    elif escolha == '4':
        listar_tarefas(tarefas)
        indice = int(input("Digite o índice da tarefa a ser removida: "))
        remover_tarefa(tarefas, indice)
        salvar_tarefas(arquivo_tarefas, tarefas)
    elif escolha == '5':
        print("Obrigado por usar o Aplicativo de Gerenciamento de Tarefas. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
