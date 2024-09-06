alunos = []
qtd_alunos = int(input("\nDigite a quantidade de alunos que deseja calcular a média: "))
total_notas = 0
media = 0
for i in range (qtd_alunos):
    nome = str(input("\nDigite o nome: "))
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    nota3 = int(input("Digite a terceira nota: "))
    total_notas = nota1 + nota2 + nota3
    media = total_notas / 3
    item = (nome, nota1, nota2, nota3, media)
    alunos.append(item)
print(len(alunos), "Alunos Adicionados.")

for item in alunos:
    print("\n|Nome|:", item[0], "|Média|: ", (item[1] + item[2] + item[3]) /3)
    media_calculo = float(item[4])

    if media_calculo >= 7:
        print("Aluno Aprovado!")
    else:
        print("Aluno Reprovado!")