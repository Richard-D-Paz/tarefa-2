num = int(input("Digite um número para descobrir seus divisores: "))

i = num


while i <= num and not i == 0 : 
    
    if num % i == 0:
    
        print(i)
    i -= 1
    
"""
faz a variavel 'i' recebr o mesmo valor de 'num'

Enquanto i for igual ou menor e i não for igual a 0,ele vai verificar se o resto

da divisão entre 'i' e 'num' é igual a 0. E se for verdadeira a condição ira

imprimir o número em questão, e por fim subtrai 1 e repete até 'i' ser igual 0
"""