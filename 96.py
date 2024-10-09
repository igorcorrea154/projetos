from math import factorial
def fatorial():
    v = factorial(n)
    print(v)
def mostrar():
    m = ()
    count = n
    m = str(input("deseja mostrar o calculo? ")).strip().lower()[0]
    if m == "s":
        print(f"{n}",end="")
        for c in range(0,n):
            print(f" X {count}",end="")
            count -= 1
        print(" = ",end="")

n = int(input("escolha um numero: "))
mostrar()
fatorial()