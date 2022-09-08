n1 = int(input('Insira um número inteiro: '))
n2 = int(input('Insira um segundo número inteiro: '))

if n1 < n2:
    for c in range(n1,n2+1):
        print(c)

else:
    for c in range(n2,n1+1):
        print(c)