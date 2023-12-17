i = 1 #sobe até 9
a = 1 #sobe muito

#enquanto verdade escreva "i x a: ", (i * a) e some +1 a i até ser igual ou maior que 11
while i < 11 and a < 11:
    print(i, "x", a,": ",i * a)
    i += 1
# se i for
    if i >= 11 and not a >= 11:
        a+= 1
        i = 1
# quando ambas chegam a 10 eles encerram a contagem
    elif i == 11 and a == 11:        
        break

"""
        while i <= 10 and a <= 10:
    print(i, "x", a,": ",i * a)
    i += 1
    if a == 10:
        a+= 1
        
        print(a)
"""