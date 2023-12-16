print("\n","Vamos verificar dois número e dizer qual é o maior dentre os dois, ou se são iguais: ", "\n", "\n")

num1 = float(input("1º Número: "))
num2 = float(input("2º Número: "))

if num1 > num2:
    print("dentre os dois, o maior número é: ", num1)

elif num1 < num2:
    print("dentre os dois, o maior número é: ", num2)

elif num1 == num2:
    print("os números são iguais!", num1, " = ", num2)