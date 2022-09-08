'''A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
'''

n = int(input('Qual é o termo a ser encontrado? : '))
ult = 1
penult = 1

if (n==1) or (n==2):
    print('1')
else:
    for c in range(2,n):
        termo = ult + penult
        penult = ult
        ult = termo
        c += 1
    print (termo)