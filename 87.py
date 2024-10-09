from datetime import date
data = date.today().year
lista = dict()
lista["nome"] = str(input("nome: "))
lista["data"] = int(input("data de nascimento: "))
lista["carteira de trabalho"] = int(input("numero da carteira: "))
idade = data - lista["data"]
if lista["carteira de trabalho"] != 0:
    lista["ano de contratacao"] = int(input("ano de contratação: "))
    aposentadoria = (lista["ano de contratacao"] - lista["data"]) + 35
    ano_contratado = lista["ano de contratacao"] + 35
    lista["salario"] = float(input("salario: "))
print("-="*30)
print(f" - seu nome é: {lista["nome"]}")
print(f" - tem: {idade} anos")
print(f" - id da carteira de trabalho: {lista['carteira de trabalho']}")
print(f" - ano de contratação: {lista['ano de contratacao']}")
print(f" - salario: {lista['salario']}")
print(f" - vai se aposentar em: {ano_contratado}, com {aposentadoria} anos")
