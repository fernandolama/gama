nome = input('Digite seu nome: ')

while len(nome) < 3:
    nome = input('Seu nome deve conter mais de 3 caracteres. Digite um nome válido: ')
print('Nome válido.')

idade = int(input('Digite sua idade: '))

while not (idade > 0 and idade < 150):
    idade = int(input('Sua idade deve ser entre 0 e 150 anos. Digite uma idade válida: '))
print('Idade válida.')

salario = float(input('Digite seu salário: '))

while salario < 0:
    salario = float(input('Seu salário não pode ser menor do R$ 0.00. Digite um valor válido: '))
print('Salário válido.')

sexo = input('Digite "f" para sexo feminino ou "m" para masculino: ').lower()

while sexo != "f" and sexo != "m":
    sexo = input('Valor inválido. Digite "f" para sexo feminino ou "m" para masculino: ')
print('Sexo válido.')

est_civil = input('Digite "s" para solteiro(a), "c" para casado(a), "v" para viúvo(a) ou "d" para divorciado(a): ').lower()

while est_civil not in "scvd":
    est_civil = input('Valor inválido. Digite "s" para solteiro(a), "c" para casado(a), "v" para viúvo(a) ou "d" para divorciado(a): ')
print('Estado civil válido.  Fim do programa.')