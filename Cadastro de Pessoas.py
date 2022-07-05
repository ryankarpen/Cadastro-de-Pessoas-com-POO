class Pessoa:
    def __init__(self, nome, nascimento, sexo, cpf):
        self.nome = nome
        self.nascimento = nascimento
        self.sexo = sexo
        self.cpf = cpf

    def idade(self):
        from datetime import date
        atual = date.today().year
        return atual - self.nascimento

    def __str__(self):
        return f'Dados pessoais cadastrados: \n' \
               f'Nome: {self.nome} \n' \
               f'Idade: {Pessoa.idade(self)} \n' \
               f'Sexo: {self.sexo} \n' \
               f'Cpf: {self.cpf}'


pessoa1 = Pessoa('Ryan Lucas Karpen', 2002, 'Masculino', 22222222222)
print(pessoa1)


