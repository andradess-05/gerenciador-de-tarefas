
agenda = []

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }
    
    agenda.append(contato)
    print(f"Contato {nome} adicionado com sucesso!\n")

def listar_contatos():
    if len(agenda) == 0:
        print("A agenda está vazia!\n")
        return
    
    print("Contatos da agenda:")
    for i, contato in enumerate(agenda):
        print(f"{i+1}. Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
    print()

def buscar_contato():
    busca = input("Digite o nome do contato que deseja buscar: ")
    encontrados = [c for c in agenda if busca.lower() in c["nome"].lower()]
    
    if len(encontrados) == 0:
        print("Nenhum contato encontrado!\n")
        return
    
    print("Contatos encontrados:")
    for contato in encontrados:
        print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
    print()

def menu():
    while True:
        print("=== AGENDA DE CONTATOS ===")
        print("1 - Adicionar contato")
        print("2 - Listar contatos")
        print("3 - Buscar contato")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_contato()
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            buscar_contato()
        elif opcao == "4":
            print("Saindo da agenda... Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.\n")

# Inicia o programa
menu()
