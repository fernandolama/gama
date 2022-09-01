area = float(input("Qual é a area a ser pintada, em m2? "))
litros = area // 3

preco = 80
capacidade = 18

latas = int(litros // capacidade)
total = float(latas * preco)

print ('Você usará',latas, 'latas de tinta e pagará R$',total,'.')