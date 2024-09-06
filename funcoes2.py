def encontrar_maior_numero(lista):
    maior = lista[0]

    for numero in lista:
        if numero > maior:
            maior = numero
    
    return maior

lista_de_numeros = ([10, 88, 12, 80000, 241, 74])
maior_numero = encontrar_maior_numero(lista_de_numeros)
print("O Maior número é: ", maior_numero)