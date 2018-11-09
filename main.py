from conta import Conta
from cliente import Cliente

cliente1 = Cliente('Eric Gomes', '123.345.456-70', 33)

print(cliente1.nome)

contaEric = Conta(cliente1, 10.50, 50.00)

print(contaEric.cliente, '\nSaldo:', contaEric.saldo)


