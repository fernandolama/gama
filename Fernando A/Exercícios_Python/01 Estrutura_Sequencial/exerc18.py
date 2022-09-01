arq = float(input('Digite o tamanho (em MB) do arquivo que deseja fazer o download: '))
vel = int(input('Digite a velocidade de sua conexão (em Mbps): '))

print('O tempo estimado para a realização do download desse arquivo é:', (arq / vel)/60)