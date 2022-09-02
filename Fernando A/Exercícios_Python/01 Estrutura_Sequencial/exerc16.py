import math

area = float(input("Qual é a area a ser pintada, em m²? "))
litros = area / 3

preco = 80
capacidade = 18

latas = litros / 18
latas_arr = math.ceil(latas)
total = latas_arr * 80

print ('Você usará',latas_arr, 'latas de tinta e pagará R$',total,'.')