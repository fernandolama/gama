prod1 = float(input('Qual é o preço do produto x? : R$ '))
prod2 = float(input('Qual é o preço do produto y? : R$ '))
prod3 = float(input('Qual é o preço do produto z? : R$ '))

if prod1 < prod2 and prod1 < prod3:
    print('Você deve comprar o produto x.')

if prod2 < prod1 and prod2 < prod3:
    print('Você deve comprar o produto y.')

if prod3 < prod1 and prod3 < prod2:
    print('Você deve comprar o produto z.')