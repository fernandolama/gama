l1 = float(input('Informe um lado do triângulo: '))
l2 = float(input('Informe o segundo lado do triângulo: '))
l3 = float(input('Informe o terceiro lado do triânglo: '))

if (l1 + l2 > l3) or (l1 + l3 > l2) or (l2 + l3 > l1):
    if l1 == l2 and l1 == l3:
        print('Essa figura pode ser um triângulo. Um triângulo equilátero, mais precisamente.')

    if l1 != l2 and l1 != l3 and l2 != l3:
        print('Essa figua pode ser um triângulo. Um triângulo escaleno, mais precisamente.')

    if (l1 == l2 and l3 < l1) or (l2 == l3 and l1 < l2) or (l3==l1 and l2<l1):
        print('Essa figura pode ser um triângulo. Um triângulo isósceles, mais precisamente.')