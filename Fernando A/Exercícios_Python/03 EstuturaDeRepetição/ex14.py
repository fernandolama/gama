pares = 0
impares = 0

for n in range(10):
    if int(input('Insira um número: ')) % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f'Pares: {pares}\nÍmpares: {impares}')