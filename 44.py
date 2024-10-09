produto = int(input("qual o preco do produto? "))
n1 = produto * 0.10
n2 = produto * 0.05
n3 = produto * 0.20
print("1- a vista, dinheiro / cheque: 10% de desconto")
print("2- a vista, cartao: 5% de desconto")
print("3- em até 2x no cartao: preco normal")
print("4- 3x ou mais no cartao: 20% de juros")
pagamento = int(input("qual a forma de pagamento? "))
if pagamento == 1:
    print(produto - n1)
elif pagamento == 2:
    print(pagamento - n2)
elif pagamento == 3:
    print(produto)
else:
    print(produto + n3)