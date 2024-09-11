class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf, rg):
        super().__init__(nome)
        self.cpf = cpf
        self.rg = rg

class PessoaJuridica(Pessoa):
    def __init__(self, nome, cnpj, inscricao_estadual):
        super().__init__(nome)
        self.cnpj = cnpj
        self.inscricao_estadual = inscricao_estadual

#Exemplo de uso:
PessoaFisica = PessoaFisica("Maria Alves", "059641321-60", "1.123.456", )
print(PessoaFisica.nome, PessoaFisica.cpf, PessoaFisica.rg)

PessoaJuridica = PessoaJuridica("Senior", "12.345.678/9101-11", "46532132")
print(PessoaJuridica.nome, PessoaJuridica.cnpj, PessoaJuridica.inscricao_estadual)
