a = 80000
taxa_a = 1.03

b = 200000
taxa_b = 1.015

ano = int(0)

while a < b:
    a=a*taxa_a
    b=b*taxa_b
    ano=ano+1

print('A população do país A ultrapassará a do país B após', ano,'anos.')