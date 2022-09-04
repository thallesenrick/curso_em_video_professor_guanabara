from time import sleep
primeiro = int(input('\033[93mDigite o primeiro valor: '))
segundo = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 8:
    print('''\033[94m    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] exponenciação
    [ 6 ] dividir
    [ 7 ] subtrair
    [ 8 ] sair do programa\033[m''')
    opcao = int(input('\033[93m>>>>> Qual é multi sua opção? '))
    if opcao == 1:
        soma = primeiro + segundo
        print(f'A soma entre {primeiro} + {segundo} é {soma}')
    elif opcao == 2:
        multi = primeiro * segundo
        print(f'O resultado de {primeiro} x {segundo} é {multi}')
    elif opcao == 3:
        if primeiro > segundo:
            maior = primeiro
        elif segundo > primeiro:
            maior = segundo
        elif segundo == primeiro:
            print(f'Os números são iguais')
        print(f'Entre {primeiro} e {segundo} o maior é {maior}')
    elif opcao == 4:
        print('Informe os números novamente: ')
        primeiro = int(input('Digite o primeiro valor: '))
        segundo = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        expo = primeiro ** segundo
        print(f'O número {primeiro} elevado multi {segundo} é {expo}')
    elif opcao == 6:
        divisao = primeiro / segundo
        print(f'A divisão entre {primeiro} e {segundo} é {divisao:.2f}')
    elif opcao == 7:
        subtracao = primeiro - segundo
        print(f'A subtração entre {primeiro} e {segundo} é {subtracao}')
    elif opcao == 8:
        print('Finalizando ...')
        sleep(1.5)
        print('Fim do programa! Volte sempre!')
    else:
        print('Opção inválida. Tente novamente')
    print('\033[91m=-=' * 10)
    sleep(1.5)
