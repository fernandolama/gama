n1 = float(input('Insira a primeira nota parcial: '))
n2 = float(input('Insira a segunda nota parcial: '))
media = (n1 + n2)/2

if media >= 7 and media <= 9.9:
    print('Aprovado')

if media < 7:
    print('Reprovado')

if media == 10:
    print('Aprovado com Distinção')