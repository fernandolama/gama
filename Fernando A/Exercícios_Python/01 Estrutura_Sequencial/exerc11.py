from pickletools import read_bytes4


int1 = int(input('Digite um número inteiro: '))
int2 = int(input('Agora, digite mais um número inteiro: '))
real = float(input('Por fim, digite um número real: '))

print('Sabe quanto é o produto do dobro do primeiro com a metade do segundo? É', (int1 * 2) * (int2 / 2),"!")
### Como reduzir a quantidade de casas decimais desse resultado a 0 casas?

print('Legal, né? E a soma do triplo do primeiro com o terceiro, você suspeita quanto é? Muito bem! É', (int1 * 3) + real,"!")
print('Essa é mais difícil: quanto é o terceiro elevado ao cubo? Exato! É', real**3,"!")