pesoLim = 50
peso = float(input('Digite a quantidade de peixe trazido (em quilos): '))
if peso > pesoLim:
    excesso = peso - pesoLim
    multa = excesso*4
    print ('A multa será de R$', float(multa),'.')