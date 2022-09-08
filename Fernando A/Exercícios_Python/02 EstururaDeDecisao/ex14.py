n1 = float(input('Insira a primeira nota parcial: '))
n2 = float(input('Insira a segunda nota parcial: '))
media = (n1 + n2)/2

if media >= 9 and media <= 10:
    print('Parcial 1: ',n1,'\n'
    'Parcial 2: ',n2,'\n'
    'Média: ',media, '\n'
    'Conceito: A\n'
    'APROVADO!')

elif media >= 7.5 and media < 9:
    print('Parcial 1: ',n1,'\n'
    'Parcial 2: ',n2,'\n'
    'Média: ',media, '\n'
    'Conceito: B\n'
    'APROVADO!')

elif media >= 6 and media < 7.5:
    print('Parcial 1: ',n1,'\n'
    'Parcial 2: ',n2,'\n'
    'Média: ',media, '\n'
    'Conceito: C\n'
    'APROVADO!')

elif media >= 4 and media < 6:
    print('Parcial 1: ',n1,'\n'
    'Parcial 2: ',n2,'\n'
    'Média: ',media, '\n'
    'Conceito: D\n'
    'REPROVADO!')

elif media > 0 and media < 4:
    print('Parcial 1: ',n1,'\n'
    'Parcial 2: ',n2,'\n'
    'Média: ',media, '\n'
    'Conceito: E\n'
    'REPROVADO!')

else:
    print('Valor inválido')