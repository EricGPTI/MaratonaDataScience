"""
Crie um software de gerenciamento bancário.
Esse software poderá ser capaz de criar clientes e contas.
Cada cliente possui nome, cpf idade
cada conta possui um cliente, saldo, limite, sacar, depositar e consultar saldo.
"""

class Cliente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def __str__(self):
        return "Nome: " + self.nome + "\nCPF: " + self.cpf + "\nIdade: " + str(self.idade)
