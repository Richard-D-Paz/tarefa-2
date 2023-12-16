num = float(input("Digite o valor para ser identificado se é positivo, negativo ou igual a zero: "))



while num == 0:
    print("Valor inválido")

    num = float(input("Digite o valor para ser identificado se é positivo, negativo ou igual a zero: "))

if num > 0:
        print("este número é positivo")

elif num < 0:
        print("este número é negativo")