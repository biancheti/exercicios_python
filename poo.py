class Pessoa:
    
    def __init__(self, nome, idade):       #Método inicializador construtor
        self.nome = nome                   #Atributo de nome
        self.idade = idade                 #Atributo de idade
    
    def mostrar_informacoes(self):
        print("|Nome|: ", self.nome, "|Idade|: ", self.idade)

if __name__ == "__main__":                 #Criando um objeto da classe instância
    pessoa1 = Pessoa("João", 30)
    pessoa2 = Pessoa("Ana", 28)
    pessoa3 = Pessoa("Julia", 25)
    pessoa1.mostrar_informacoes()
    pessoa2.mostrar_informacoes()
    pessoa3.mostrar_informacoes()
