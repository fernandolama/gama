a = int(input('Insira a população do país A: '))
taxa_a = float(input('Insira a taxa de crescimento anual do país A: '))

b = int(input('Insira a população do país B: '))
taxa_b = float(input('Insira a taxa de crescimento anual do país B: '))

ano = int(0)

while taxa_a < taxa_b:
    print('A taxa de crescimento anual do país A deve ser necessariamente maior do que o percentual correspondente do país B: ')
    taxa_a = float(input('Insira a taxa de crescimento anual do país A: '))
    taxa_b = float(input('Insira a taxa de crescimento anual do país B: '))

while b <= a:
    print('A população inicial do país A deve ser necessariamente maior do que o valor correspondente do país B.')
    a = int(input('Insira a população do país A: '))
    b = int(input('Insira a população do país B: '))

while a <= b:
    a=a*taxa_a
    b=b*taxa_b
    ano=ano+1

print('A população do país A ultrapassará a do país B após', ano,'anos.')