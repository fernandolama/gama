n1 = float(input('Insira a primeira nota parcial: '))
n2 = float(input('Insira a segunda nota parcial: '))
media = (n1 + n2)/2

if media >= 7:
    if media == 10:
            print('Aprovado com Distinção')
    
    else:
        print('Aprovado')
else:
    print('Reprovado')