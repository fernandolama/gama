nota = float(input("Insira uma nota entre 0 e 10: "))

while not(nota >= 0 and nota <= 10):
   print('Valor inválido.')
   nota = float(input('Digite um valor válido: '))

print('Nota válida. Fim do programa')