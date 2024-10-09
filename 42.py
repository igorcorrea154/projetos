n1 = int(input("digite o comprimento da reta A: "))
n2 = int(input("digite o comprimento da reta B: "))
n3 = int(input("digite o comprimento da reta C: "))
if n1 + n2 > n3 and n2 + n3 > n1 and n1 + n3 > n2:
    if n1 == n2 and n1 == n3:
        print("esse triangulo é equilatero")
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print("esse triangulo é isosceles")
    else:
        print("esse triangulo é escaleno")
else:
    print("nao pode formar um triangulo")