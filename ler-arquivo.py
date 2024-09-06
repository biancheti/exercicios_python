with open("produto.txt", "r", encoding="utf-8") as arquivo:
    #Ler o conteúdo do arquivo linha por linha
    linhas = arquivo.readlines()

    #Mostrar as informações do arquivo .txt
    for linha in linhas:
        print(linha.strip())