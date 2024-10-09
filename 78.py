valor = list()
n = "s"
adicionar = 0
while n in "s":
    if n == "s":
        add = int(input("digite um valor: "))
        if add not in valor:
            valor.append(add)
        else:
            print("valor duplicado, nao foi adicionado")
        n = str(input("DESEJA CONTINUAR? ")).strip().lower()[0]
valor_crescente = sorted(valor)
print(valor_crescente)
