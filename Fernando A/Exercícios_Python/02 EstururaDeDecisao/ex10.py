turno = input('Em que turno você estuda? Digite "M" para matutino, "V" para vespertino e "N" para noturno: ')

if turno.upper() == 'M':
    print('Bom dia!')

elif turno.upper() == 'V':
    print('Boa tarde!')

elif turno.upper() == 'N':
    print('Boa noite!')

else:
    print('Valor inválido!') 