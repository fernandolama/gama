num = int(input('Informe um número de 1 a 10: '))

while num < 0 or num > 10:
    num = int(input('Número inválido. Informe um número de 1 a 10: '))

print('Calculando a tabuada...\n')
print('Tabuada de', num,':')

for c in range(1,11):
    print(f'{num} X {c} = {num*c}')

print('Fim do programa.')