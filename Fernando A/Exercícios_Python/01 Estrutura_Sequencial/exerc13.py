alt = float(input('Qual é a sua altura em metros? '))

p_id_h = (72.7 * alt) - 58
p_id_h = round(p_id_h, 1)
p_id_m = (62.1 * alt) - 44.7
p_id_m = round(p_id_m, 1)

print ('Se você for um homem, seu peso ideal é', p_id_h,'''.
Caso seja uma mulher, seu peso ideal é''', p_id_m,'.')
