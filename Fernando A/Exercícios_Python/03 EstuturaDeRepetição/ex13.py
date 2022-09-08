'''
Faça um programa que peça dois números, base e expoente,
calcule e mostre o primeiro número elevado ao segundo 
número. Não utilize a função de potência da linguagem.
'''

base = float(input('Insira a base: '))
exp = int(input('Insira o expoente: '))

potencia = 1
c=1

while c <= exp:
    potencia *= base
    c += 1

print(base,'^',exp,'=',potencia)