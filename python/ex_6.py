nota = float(input("Digite a nota do aluno: "))

while 0 < nota > 10:
    print("ERR0R")

    nota = float(input("Digite a nota do aluno: "))

if nota < 6:
    print("Nota F")

elif 6 <= nota <= 7:
    print("Nota D")

elif 7 <= nota <= 8:
    print("Nota C")
    
elif 8 <= nota <= 9:
    print("Nota B")

elif 9 < nota <= 10:
    print("Nota A")
