alunos = []
records_pessoais = []

wod = "\n|WOD|: Murph \n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n| 1 Mile Run \n| 100 Pull Ups \n| 200 Push Ups \n| 300 Squats\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n"

def menu():
    print("               |MENU|               ")
    print("____________________________________")
    print("                                    ")
    print("   |1| * |Mostrar Treino do Dia|    ")
    print("   |2| * |Fazer Check-in|           ")
    print("   |3| * |Ver Check-ins do Dia|     ")
    print("   |4| * |Cancelar Check-In|        ")
    print("   |5| * |Adicionar Personal Record|")
    print("   |6| * |Seus Personal Records|    ")
    print("   |7| * |Sair do App|              ")
    print("____________________________________")

    opcao = str(input("\nEscolha Uma das Opções acima: "))

    if opcao == '1':
        mostrar_treino()
    elif opcao == '2':
        fazer_checkin()
    elif opcao == '3':
        ver_checkins()
    elif opcao == '4':
        cancelar_checkin()
    elif opcao == '5':
        adicionar_records()
    elif opcao == '6':
        mostrar_records()
    elif opcao == '7':
        sair_app()
    else:
        print("\nAtenção! Digite Somente Números de 1 à 7. Tente Novamente.\n")
        return menu()
        
def mostrar_treino():
    if wod == "":
        print("\nNenhum WOD cadastrado até o momento...\n")

    print(wod)
    return menu()

def fazer_checkin():
    print("\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("Vamos Registrar seu Check-In Para Hoje:")
    nome = str(input("\nDigite seu Nome: "))

    try:
        id = int(input("Digite seu ID: "))

        print("\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        print(" |Horários Disponíveis|:")
        print(" |1| - |07:30|          ")
        print(" |2| - |09:00|          ")
        print(" |3| - |12:00|          ")
        print(" |4| - |18:15|          ")
        print(" |5| - |19:15|          ")
        print(" |6| - |20:30|          ")
        print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n")
        
        posicao_horario = int(input("Digite o Número Correspondente ao Horários que Você Deseja: "))
        
        if posicao_horario >= 1 and posicao_horario <= 6:
            print("\nCheck-in Realizado com Sucesso!\n")
            horario =  retornar_horario(posicao_horario)
            registro = (id, nome, posicao_horario,horario)
            alunos.append(registro)
            return menu()
        else:
            print("\nAtenção! Essa Opção é Inválida. Tente Novamente.")
            return fazer_checkin()
        
    except ValueError:
        print("\nOops! Use Somente Números. Tente Novamente.")
        return fazer_checkin()
          
def retornar_horario(posicao):
    opcoes = {
        1: "07:30",
        2: "09:00",
        3: "12:00",
        4: "18:15",
        5: "19:15",
        6: "20:30",
    }
    return opcoes.get(posicao, "Posicao Inválida.")

def ver_checkins():
    if alunos == []:
        print("\nNenhum Aluno Fez Check-in Até o Momento.\n")
        return menu()
    
    print("\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("\n|Lista de Check-In|\n")
    
    for registro in alunos:
        print("|ID|: ", registro[0], "|Nome|: ", registro[1], "   |Horário|: ", registro[3])
        print("_________________________\n")

    return menu()

def cancelar_checkin():
    if alunos == []:
        print("\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        print("Você Não Fez Check-In até o Momento.\n")
        return menu()
    
    try:
        id = int(input("\nDigite seu ID para Cancelarmos seu Check_In: "))

        for aluno in alunos:
            if aluno[0] == id:
                alunos.remove(aluno)
                print("\nCheck-In do Aluno com ID", id, "Foi Cancelado.\n")
                return menu()
            
        else:
            print(f"Oops! ID {id} Não Encontrado. Tente novamente. ")
            return cancelar_checkin()
    
    except ValueError:
        print("\nOops! Use Somente Números. Tente Novamente.")
        return cancelar_checkin()

def adicionar_records():
    try:

        print("\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        print(" |MOVIMENTOS|:          ")
        print(" |1| - |Power Clean|    ")
        print(" |2| - |DeadLift|       ")
        print(" |3| - |Snatch|         ")
        print(" |4| - |Push Press|     ")
        print(" |5| - |Clean And Jerk| ")
        print(" |6| - |Cluster|        ")
        print(" |7| - |Thruster|       ")
        print(" |8| - |Push Jerk|      ")
        print(" |9| - |Over Head Squat|")
        print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n")


        print("\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        print("Vamos Registrar seu Personal Record: ")
        posicao_movimento = int(input("Digite o Número Correspondente ao Exercício que Você Deseja Adicionar o PR: "))

        if posicao_movimento >= 1 and posicao_movimento <= 9:
                peso = int(input("\nDigite o Peso da Carga Máxima em Kg (Somente Números): "))
                movimento = retornar_movimento(posicao_movimento)
                registro = (peso, posicao_movimento, movimento)
                records_pessoais.append(registro)
                print("\nPersonal Record Adicionado com Sucesso!\n")
                return menu()
        else:
                print("\nAtenção! Digite um Número Válido. Tente Novamente.")
                return adicionar_records()
    
    except ValueError:
        print("\nOops! Use Somente Números. Tente Novamente.")
        return adicionar_records()

def retornar_movimento(posicao):
    opcoes = {
        1: "Power Clean",
        2: "DeadLift",
        3: "Snatch",
        4: "Push Press",
        5: "Clean And Jerk",
        6: "Cluster",
        7: "Thruster",
        8: "Push Jerk",
        9: "Over Head Squat",
    }
    return opcoes.get(posicao, "Posição Inválida.")

def mostrar_records():
    if records_pessoais == []:
        print("\nNenhum Personal Record Adicionado até o Momento.\n")
        return menu()
    
    print("\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("  |Personal Records|  \n")

    for registro in records_pessoais:
        print("|Peso|: ", registro[0], " Kg ", "|Movimento|: ", registro[2])
    print("\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n")

    return menu()

def sair_app():
    print("\nAté Logo...\n")
    print("Aplicativo encerrado.")
    exit

if __name__ == "__main__":
    menu()