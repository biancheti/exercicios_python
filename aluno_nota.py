qtd_notas = int(input("Digite a quantidade de notas: "))
total_de_notas = 0

print("********************")
aluno = input("Digite o nome do aluno: ")
for i in range(qtd_notas):

    nota = int(input("Digite a nota: "))
    total_de_notas += nota
    media = total_de_notas / qtd_notas

if media >= 6:
    print("\n********************")
    print((aluno), ("|"), (media), ("|"), "APROVADO!")
    print("********************")
else:
    print("\n********************")
    print((aluno), ("|"), (media) ("|"), "Reprovado.")
    print("********************")