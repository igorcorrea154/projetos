frase = str(input("digite uma frase: ")).strip().lower().split()
junto = "".join(frase)
if junto == junto[::-1]:
    print("é um palimdromo")
else:
    print("nao é um palimdromo")