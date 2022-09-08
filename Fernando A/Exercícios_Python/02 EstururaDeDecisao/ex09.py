n1 = float(input('Digite um número: '))
n2 = float(input('Digite um segundo número: '))
n3 = float(input('Digite um terceiro número: '))

if n1 < n2 and n1 < n3 and n2 < n3:
    print('Os 3 números digitados em ordem crescente são: ', n1, ',', n2,'e',n3,'.')

if n1 < n3 and n3 < n2 and n1 < n3:
    print('Os 3 números digitados em ordem crescente são: ', n1, ',', n3,'e',n2,'.')

if n2 < n1 and n2 < n3 and n1 < n3:
    print('Os 3 números digitados em ordem crescente são: ', n2, ',', n1,'e',n3,'.')

if n2 < n3 and n2 < n1 and n3 < n1:
    print('Os 3 números digitados em ordem crescente são: ', n2, ',', n3,'e',n1,'.')

if n3 < n1 and n3 < n2 and n1 < n2:
    print('Os 3 números digitados em ordem crescente são: ', n3, ',', n1,'e',n2,'.')

if n3 < n1 and n3 < n2 and n2 < n1:
    print('Os 3 números digitados em ordem crescente são: ', n3, ',', n2,'e',n1,'.')