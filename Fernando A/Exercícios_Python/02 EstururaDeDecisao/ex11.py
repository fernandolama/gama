salario = float(input('Digite o valor do salário do colaborador: R$ '))

if salario <= 280:
    reajuste = .2
elif salario <= 700:
    reajuste = .15
elif salario <= 1500:
    reajuste = .1
else:
    reajuste = .05

print('Salário antes do reajuste:', salario)
print('Reajuste aplicado: ', int(reajuste*100), '%', sep='')
print('Aumento aplicado: ', reajuste*salario)
print('Novo salário: ', salario + reajuste*salario)