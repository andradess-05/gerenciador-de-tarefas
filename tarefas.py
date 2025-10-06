# Projeto: Lista de Tarefas Simples
# Autor: Estudante
# Descrição: Permite adicionar, ver e remover tarefas de uma lista.

tarefas = []

def mostrar_menu():
    print("\n===== Lista de Tarefas =====")
    print("1. Ver tarefas")
    print("2. Adicionar tarefa")
    print("3. Remover tarefa")
    print("4. Sair")

def ver_tarefas():
    if not tarefas:
        print("Nenhuma tarefa na lista!")
    else:
        print("\nTarefas atuais:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")

def adicionar_tarefa():
    tarefa = input("Digite a tarefa que deseja adicionar: ")
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def remover_tarefa():
    ver_tarefas()
    if tarefas:
        try:
            numero = int(input("Digite o número da tarefa que deseja remover: "))
            if 1 <= numero <= len(tarefas):
                tarefa_removida = tarefas.pop(numero - 1)
                print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
            else:
                print("Número inválido!")
        except ValueError:
            print("Digite um número válido!")

# Loop principal
while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        ver_tarefas()
    elif opcao == "2":
        adicionar_tarefa()
    elif opcao == "3":
        remover_tarefa()
    elif opcao == "4":
        print("Saindo... Até mais!")
        break
    else:
        print("Opção inválida! Tente novamente.")
