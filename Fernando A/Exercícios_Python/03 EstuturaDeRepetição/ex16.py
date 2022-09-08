'''A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500.'''

ant=0
prox=0

while prox < 500:
    print(prox)
    prox += ant
    ant = prox - ant
    
    if  prox == 0:
        prox = prox + 1