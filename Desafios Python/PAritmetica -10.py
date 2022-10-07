from time import sleep
primeiro = int(input('Prmeiro termo: '))
razao = int(input('Qual é a razão: '))
for c in range(1, 11):
    print('{}º)'.format(c), primeiro, end='  -  ')
    primeiro += razao
    sleep(0.8)
print('FIM')