n1 = int(input('Insira um número inteiro: '))
n2 = int(input('Insira um segundo número inteiro: '))

soma = 0

if n1 < n2:
    for c in range(n1+1,n2):
        soma+=c
    print('A soma dos números compreendidos entre os dois números inseridos é',soma,'.')

else:
    for c in range(n2+1,n1):
        soma+=c
    print('A soma dos números compreendidos entre os dois números inseridos é',soma,'.')