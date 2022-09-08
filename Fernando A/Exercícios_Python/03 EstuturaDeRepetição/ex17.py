'''Faça um programa que calcule o fatorial de um número
inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120'''

num = int(input('Insira um número inteiro: '))
result = 1

for c in range(1, num+1):
    result *= c

print('O fatorial de',num,'é', result,'.')