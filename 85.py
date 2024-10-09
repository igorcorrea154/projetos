lista = dict()
nome = str(input("nome do aluno: "))
nota1 = float(input("1° nota: "))
nota2 = float(input("2° nota: "))
lista["nome"] = nome
lista["media"] = (nota1 + nota2) / 2
print(f"o nome é igual a {lista["nome"]}")
print(f"a media é igual a {lista["media"]}")
if (nota1 + nota2) / 2 < 7:
    print("Ele está reprovado")
else:
    print("Ele está aprovado")