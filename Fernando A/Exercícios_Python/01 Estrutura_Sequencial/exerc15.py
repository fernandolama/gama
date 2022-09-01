valor_hora = float(input('Qual é o valor de sua hora trabalhada? '))
hora_mes = float(input('E a quantidade de horas trabalhadas no mês? '))
salbr = valor_hora * hora_mes
ir = (salbr * 11/100)
inss = (salbr * 8/100)
sind = (salbr * 5/100)
sal_liq = (salbr - ir - inss - sind)

print('+ Salário bruto: R$', salbr,'.')
print('- IR (11%): R$', ir,'.')
print('- INSS (8%): R$', inss,'.')
print('- Sindicato (5%): R$', sind,'.')
print('= Salário líquido: R$', sal_liq,'.')