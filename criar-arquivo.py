#Criar um arquivo em Python
with open("produto.txt", "w", encoding= "utf-8") as arquivo:
    #Escrever as informações.
    arquivo.write("Código: 001 \n")
    arquivo.write("Descrição: Mobi \n")
    arquivo.write("Preço: R$31.000 \n")
    arquivo.write("Qtd: 1 \n")
    
    arquivo.write("\n")
    arquivo.write("Código: 002 \n")
    arquivo.write("Descrição: Renegade \n")
    arquivo.write("Preço: R$90.000 \n")
    arquivo.write("Qtd: 1 \n")