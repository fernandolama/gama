n1 = float(input('Digite um número: '))
n2 = float(input('Digite um segundo número: '))
n3 = float(input('Digite um terceiro número: '))

if n1 > n2 and n1 > n3:
    print('Dentre os números digitados, o maior é: ', n1,'.')

if n2 > n1 and n2 > n3:
    print('Dentre os números digitados, o maior é: ', n2,'.')

if n3 > n1 and n3 > n2:
    print('Dentre os números digitados, o maior é: ', n3,'.')