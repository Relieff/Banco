from time import sleep

print('='*50)
print('---Banco Fukujima---'.center(50))
print('='*50)

print('Carregando')
sleep(1)
print('[|]')
sleep(0.5)
print('[/]')
sleep(0.5)
print('[--]')
sleep(0.5)
print('[|]')
sleep(1)
print('Carregamento completo! Bem vindo(a)!')
print('-'*20)
sleep(1)

dinheiro = 0
total = dinheiro
totalced = 0
cedula = 50


while True:
    dinheiro = int(input('Digite o valor em R$: '))
    print('')
    resp = str(input('Deseja finalizar a operação? [S/N] ')).strip().upper()[0]
    print('')


    if total >= cedula:
        total -= cedula
        totalced += 1
    else:

        print(f'O dinheiro sacado foi de R${dinheiro} sendo {totalced} cedulas de {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalced = 0
        if total == 0:
            break

    if resp == 'S':
        print('Encerrando operação . . .')
        sleep(1)
        break
                #Depois de fazer a primeira parte do programa ele pula pra segunda
    op = str(input('Deseja corrigir a operação? [S/N] ')).strip().upper()[0]

    if op == 'N':
        print('Encerrando operação . . .')
        sleep(1)
        break

print('')
print('-'*30)
print('Operação encerrada com suscesso, volte sempre! ')
