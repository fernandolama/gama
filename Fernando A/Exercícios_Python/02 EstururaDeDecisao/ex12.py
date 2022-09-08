horas = float(input('Digite a quantidade de horas trabalhadas: ')) 
valor = float(input('Qual o valor da sua hora: '))
salario_bruto = round(horas * valor, 2)

ir_faixa2 = round(salario_bruto * .05, 2)
ir_faixa3 = round(salario_bruto * .10, 2)
ir_faixa4 = round(salario_bruto * .20, 2)

sindicato = round(salario_bruto * 0.03, 2)

fgts = round(salario_bruto * .11, 2)

if salario_bruto > 900 and salario_bruto <= 1500:
    print('Salário Bruto: (',horas,' h * R$',valor,')     : R$', salario_bruto,)
    print('(-) IR (5%)                               : R$', ir_faixa2,)
    print('(-) Sindicato (3%)                        : R$', sindicato,)
    print('FGTS (11%)                                : R$', fgts,)
    print('Total de descontos                        : R$', round(ir_faixa2 + sindicato, 2))
    print('Salário Líquido                           : R$', round(salario_bruto - ir_faixa2 - sindicato, 2))

elif salario_bruto > 1500 and salario_bruto <= 2500:
    print('Salário Bruto: (',horas,' h * R$',valor,')     : R$', salario_bruto,)
    print('(-) IR (10%)                              : R$', ir_faixa3,)
    print('(-) Sindicato (3%)                        : R$', sindicato,)
    print('FGTS (11%)                                : R$', fgts,)
    print('Total de descontos                        : R$', round(ir_faixa3 + sindicato, 2))
    print('Salário Líquido                           : R$', round(salario_bruto - ir_faixa3 - sindicato, 2))

elif salario_bruto > 2500:
    print('Salário Bruto: (',horas,' h * R$',valor,')     : R$', salario_bruto,)
    print('(-) IR (20%)                              : R$', ir_faixa4,)
    print('(-) Sindicato (3%)                        : R$', sindicato,)
    print('FGTS (11%)                                : R$', fgts,)
    print('Total de descontos                        : R$', round(ir_faixa4 + sindicato, 2))
    print('Salário Líquido                           : R$', round(salario_bruto - ir_faixa4 - sindicato, 2))

else:
    print('Salário Bruto: (',horas,'h * R$',valor,')       : R$', salario_bruto,)
    print('(-) IR (Isento)                           : R$ 0.0')
    print('(-) Sindicato (3%)                        : R$', sindicato,)
    print('FGTS (11%)                                : R$', fgts,)
    print('Total de descontos                        : R$', sindicato,)
    print('Salário Líquido                           : R$', round(salario_bruto - sindicato, 2))