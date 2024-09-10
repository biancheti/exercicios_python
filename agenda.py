import sys

clientes = []
id_cliente = [0]

def menu():
    print("\n****      |Menu|      ****")
    print(" |1| - Inserir Cliente(s)   ")
    print(" |2| - Listar Clientes(s)   ")
    print(" |3| -      Sair            ")
    print("****                  ****\n")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        inserir()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        sair()

def inserir():
    qtd_clientes = int(input("Quantos Clientes deseja cadastrar? "))
    total_clientes = 1
    contador = 1
    while contador <= qtd_clientes:
        total_clientes += qtd_clientes
        id = (input("\nDigite o ID do Cliente: "))
        grupo = (input("Em qual grupo deseja cadastrar o Cliente: "))
        nome = (input("Digite o nome do Cliente: "))
        celular = (input("Digite o número de Cliente: "))
        email = (input("Digite o email do Cliente: "))
        data_nascimento = (input("Digite a data de nascimento: \n"))
        registro = (id, grupo, nome, celular, email, data_nascimento)
        clientes.append(registro)
        contador = contador +1
    print(len(clientes), "Cliente(s) Adicionado(s)")
    return menu()

def listar():
 
    for cliente in clientes:
        print("|ID| ", (cliente[0]) + " |Grupo| ", (cliente[1]) + " |Nome| ", (cliente[2]) + " |Celular| ", (cliente[3]) + " |Email| ", (cliente[4]) + " |Nascimento| ", (cliente[5]))

    if clientes == []:
        print("\nNenhuma informação para exibir.")
    return menu()

def sair():
    confirmacao = input("Tem certeza que deseja sair do sistema? Digite |s| para confirmar. ")

    if confirmacao.lower() == 's':
        print("\nSaindo do sistema...\n")
        quit()
    else:
        print("\nOpção Inválida.")
        print("\nVoltando para o |Menu|...")
    return menu()
    
if __name__== "__main__":
    menu()