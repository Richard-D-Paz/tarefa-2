import random

numMaq = random.randint(1, 10)

print("ACERTE O NÚMERO!!!", "\n", "\n")

numPlayer = int(input("tente adivinhar o número escolhido pela maquina de 1 a 10!!!: "))

if numMaq == numPlayer and 0 < numPlayer <= 10:
        print("TU É O BRABO!!!", numPlayer, "=", numMaq, "CHAT GPT LIXOOOOO!!!")

elif numMaq != numPlayer and 0 < numPlayer <= 10:
        print("poxa...", numPlayer, " não está certo...o correto é: ", numMaq)

else:
     print("Esse...não é um número valido")