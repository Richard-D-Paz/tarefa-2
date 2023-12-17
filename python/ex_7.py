print("\n", "Reajuste de salário", "\n", "\n")

salarioAdd = 0
salario = float(input("Digite o salário: "))
porcentagemS1 = 20
porcentagemS2 = 15
porcentagemS3 = 10
porcentagemS4 = 5

if salario <= 280:

    salarioAdd = salario/100 * porcentagemS1

    porcentgemAtual = porcentagemS1

elif 280 < salario <= 700:

    salarioAdd = salario/100 * porcentagemS2

    porcentgemAtual = porcentagemS2

elif 700 < salario <= 1500:

    salarioAdd = salario/100 * porcentagemS3

    porcentgemAtual = porcentagemS3

else:

    salarioAdd = salario/100 * porcentagemS4

    porcentgemAtual = porcentagemS4


salarioFinal = salario + salarioAdd

print("\n", "Seu salário atual é: ", salario,"\n" , " e a porcentagem a ser aumentada: ", porcentgemAtual, "\n", "O valor a ser adicionado: ", salarioAdd, "\n", "E seu salário final será: ", salarioFinal)