dados = []
print("\n********************************")
qtd_carros = int(input("Quantos Carros deseja cadastrar: "))

for i in range(qtd_carros):
    nome_carro = input("\nDigite o Nome do Carro: ")
    ano = int(input("Digite o Ano do Carro: "))
    qtd_estoque = input("Digite a Quantidade em Estoque: ")
    registro = (nome_carro, ano, qtd_estoque)
    dados.append(registro)

print(" ")
print(len(dados), "Carros Adicionados")
    
for registro in dados:
    
    print("\n|Nome| ", registro[0], "|Ano| ", registro[1], "|Qtd| ", registro[2])
    print("************************************")