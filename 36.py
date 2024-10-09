def casa():
    valor_casa = float(input("qual o valor da casa?" ))
    salario = int(input("qual o salario do comprador?" ))
    anos = int(input("quantos anos ele vai pagar esta casa?" ))
    meses = anos / 12
    prestacao = valor_casa / meses
    if prestacao > 0.30 * salario:
        print(f"a prestacao foi de {prestacao}, por isso nao foi possivel realizar o financiamento")
    elif prestacao<= 0.30 * salario:
        print(f"a prestacao foi de {prestacao}, por isso o financiamento foi possivel")

casa()