print("Fluxograma Lâmpada.")

lampada = str(input("A Lampada está plugada? Digite (S) para Sim e (N) para Não. "))

if lampada == "S":
    print("A Lampada está plugada! ")
    bulbo = str(input("O Bulbo queimou? Digite (S) para Sim e (N) para Não. "))

    if bulbo == "S":
        print("Tem que trocar o Bulbo!")
    else:
        print("Então aproveite a Luz! ")

else:
    print("Plugue a lâmpada pra resolver o problema! ")