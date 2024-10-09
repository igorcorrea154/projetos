from datetime import date, datetime
def militar():
    data = int(input("informe o ano de nascimento "))
    idade = datetime.today().year - data
    militar = 18
    m1 = idade - militar
    m2 = militar - idade
    if idade > militar:
        if m1 == 1:
            print(f"ja passou {m1} ano para se alistar, procure a junta mais proxima!!!")
        else:
            print(f"ja passou {m1} anos para se alistar, procure a junta mais proxima!!!")
    elif idade < militar:
        if m2 == 1:
            print(f"logo vc estara pronto para se alistar, aguarde mais {m2} ano")
        else:
            print(f"logo vc estara pronto para se alistar, aguarde mais {m2} anos")
    else:
        print("esta na hora de se alistar. procure a junta da sua cidade!!!")
militar()