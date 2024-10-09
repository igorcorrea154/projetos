print("digite o seu sexo abaixo")
n = str(input("M/F: ")).upper().strip()
while n not in "MF":
    n = str(input("tente novamente: ")).upper().strip()
print("seu sexo é: {}".format(n))