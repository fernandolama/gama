import math

area = float(input("Qual é a area a ser pintada, em m²? "))
litros = area / 6
litros_folga = litros + litros*.10
precoL = 80
capacidadeL = 18

precoG = 25
capacidadeG = 3.6

latas = int(litros_folga // capacidadeL)
galoes = (litros_folga - capacidadeL*latas) / capacidadeG
galoes_arr = math.ceil(galoes)
total = float(latas*precoL + galoes_arr*precoG)

print('Se optar por comprar apenas latas, usará',math.ceil(litros/capacidadeL),'e pagará R$',(math.ceil(litros/capacidadeL)*precoL),'.')
print('Caso opte por comprar apenas galões, usará',math.ceil(litros/capacidadeG),'e pagará R$',(math.ceil(litros/capacidadeG)*precoG),'.')
print('Porém, se quiser desperdiçar menos tinta, basta comprar',latas,'lata(s) e',galoes_arr,'galão(ões), pagando R$',total,'.')