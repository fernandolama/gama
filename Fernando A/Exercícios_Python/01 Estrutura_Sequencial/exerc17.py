area = float(input("Qual é a area a ser pintada, em m2? "))
litros = area // 6

precoL = 80
capacidadeL = 18

precoG = 25
capacidadeG = 3.6

latas = int(litros // capacidadeL)
totalL = float(latas * precoL)

galoes = int(litros // capacidadeG)
totalG = float(galoes * precoG)

### Latas e galões
latas_mistas = int(((litros * 0.10) + litros) / capacidadeL)
galoes_mistos = int(((litros * 0.10) + litros) / capacidadeG) 
# totalLG = float()


print('Se optar por comprar apenas latas, usará',latas,'e pagará R$',totalL,'.')
print('Caso opte por comprar apenas galões, usará',galoes,'e pagará R$',totalG,'.')
#print('Porém, se quiser desperdiçar menos tinta, basta comprar',latas_mistas,'e',galoes_mistos', pagando R$',totalLG,'.')