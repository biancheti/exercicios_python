dados = []

def menu():
    print("\n****      |Menu|      ****")
    print("|1| - Inserir Contato(s)  ")
    print("|2| - Listar Contato(s)   ")
    print("|3| - Deletar Contato     ")
    print("|4| -      Sair           ")
    print("****                  ****\n")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        inserir()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        deletar()
    elif opcao == 4:
        sair()

def inserir():
    qtd_contatos = int(input("Quantos Contatos deseja cadastrar? "))
    total_contatos = 1
    contador = 1
    while contador <= qtd_contatos:
        total_contatos += qtd_contatos
        id = (input("\nDigite o ID do Contato: "))
        grupo = (input("Em qual grupo deseja cadastrar: "))
        nome = (input("Digite o nome para ser adicionado: "))
        celular = (input("Digite o número de contato: "))
        email = (input("Digite o email do contato: "))
        data_nascimento = (input("Digite a data de nascimento: "))
        registro = (id, grupo, nome, celular, email, data_nascimento)
        dados.append(registro)
        contador = contador +1
    print(len(dados), "Contatos Adicionados")
    return menu()

def listar():
    
    for dado in dados:
        print("|ID| ", (dado[0]) + " |Grupo| ", (dado[1]) + " |Nome| ", (dado[2]) + " |Celular| ", (dado[3]) + " |Email| ", (dado[4]) + " |Nascimento| ", (dado[5]))

    if dados == []:
        print("\nNenhum dado para exibir.")
    return menu()
        

def deletar(dados):
    print("não implementado.")

def sair():
    print("não implementado.")

if __name__== "__main__":
    menu()