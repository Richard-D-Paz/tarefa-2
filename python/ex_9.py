i = 1 #sobe até 9
a = 1 #sobe muito

while True:
    print(i, "x", a,": ",i * a)
    i += 1
    if i >= 11 and not a >= 11:
        a+= 1
        i = 1
    elif i == 10 and a == 10:
        
        break
"""
        while i <= 10 and a <= 10:
    print(i, "x", a,": ",i * a)
    i += 1
    if a == 10:
        a+= 1
        
        print(a)
"""