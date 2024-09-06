
produtos = []

print("\n*************************")
qtd = int(input('Digite a quantidade de Produtos que deseja cadastrar: '))
for i in range (qtd): #Pra dentro de uma lista
    print("\n*************************")
    id = (input("Digite o ID: "))
    produto = (input("Digite a descrição do produto: "))
    quantidade = (input("Digite a quantidade do produto em estoque: "))
    item = (id,produto,quantidade)
    produtos.append(item) #Pra acrecentar na lista
   
print(len(produtos), "Produtos") #Pra aparecer a quantidade de produtos que você adicionou.

for produto in produtos:
    print(" ID:", (produto[0]) + "| Produto:", (produto[1]) + " | Qtd:", (produto[2]))
    quantidade = int(produto[2])

    if quantidade > 0:
        print("Produto com saldo em estoque.")
    else:
        print("Produto com estoque negativo.")