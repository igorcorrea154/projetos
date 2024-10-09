n = int(input("DIGITE O INICIO: "))
n2 = int(input("DIGITE A QUANTIDADE DE PASSOS: "))
n3 = int(input("DIGITE QUANTOS NUMEROS COLOCAR: "))

n1 = n + (n3 - 1) * n2
for c in range(n, n1 + n2, n2):
    print(c,end = " .. ")
    