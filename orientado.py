class Paciente:

    def __init__(self,cpf,nome,idade,email):
        print('Acessei o contrutor')
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.email = email
        