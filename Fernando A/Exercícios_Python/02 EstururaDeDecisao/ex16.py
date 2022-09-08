import math

a = int(input("Informe o valor de a: "))

if a == 0:
    print('Essa equação não é de segundo grau. Programa encerrado.')
else:
    b = int(input("Informe o valor de b: "))
    c = int(input("Informe o valor de c: "))
    
    delta = b*b - (4*a*c)

    if delta < 0:
        print('Essa equação não possui raízes reais. Pograma encerrado.')
    
    if delta == 0:
        raiz = -b / (2*a)
        print('Essa equação possui apenas uma raiz real; ela é: ', raiz,'.')
    
    if delta > 0:
        r1 = (-b + math.sqrt(delta))/(2*a)
        r2 = (-b - math.sqrt(delta))/(2*a)
        print('Essa equação possui duas raízes reais; elas são',r1,'e',r2,'.')