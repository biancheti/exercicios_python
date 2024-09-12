# Classe em Python:
# Lugar para guardar configurações, comportamentos e funcionalidades relacionadas em um
#   único lugar que pode ser replicado e modificado quantas vezes necessário

class Carro:
    def __init__(self, cor, modelo, preco):
        self.cor = cor
        self.modelo = modelo
        self.preco = preco

    def ligar_carro(self):
        print(f'Ligando o carro {self.modelo} {self.cor}')

mustang = Carro('Laranja', 'Mustang GT', '250000')
mustang.ligar_carro()