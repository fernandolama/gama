import math

arq = float(input('Digite o tamanho (em MB) do arquivo que deseja fazer o download: '))
vel = float(input('Digite a velocidade de sua conexão (em Mbps): '))
vel_MBs = vel / 8
segs = arq/vel_MBs

print('O tempo estimado para a realização do download desse arquivo é:', int(segs//60), 'min e', math.ceil(segs%60), 's')