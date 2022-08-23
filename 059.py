n1 = int(input('Primeiro valor'))
n2 = int(input('Segundo valor'))
n3 = int(input('Terceiro valor'))
n4 = int(input('Quarto valor'))
opção = 0
while opção !=5:
    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    ''')
    opção = str(input('Qual é a sua opção?'))
    if opção == 1:
        soma = n1+n2+n3+n4
        print('A soma entre {}, {}, {} e {} é {}'.format(n1,n2,n3,n4,soma))
    elif opção == 2:
          produto = n1 * n2 * n3 * n4
          print('O produto de {}x{}x{}x{} é {}'.format(n1,n2,n3,n4,produto))
    elif opção == 3:
          if n1 > n2 > n3 > n4:
              maior = n1
          else:
              maior = n2
          print('Entre {} e {} o maior é o valor {}'.format(n1,n2,maior))
    elif opção == 4:
          print('Informe os números novamente:')
          n1 = int(input('Primeiro valor'))
          n2 = int(input('Segundo valor'))
          n3 = int(input('Terceiro valor'))
          n4 = int(input('Quarto valor'))
    elif opção == 5:
          print('FINALIZAMOS.')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    print('FIM DO PROGRAMA! VOLTE SEMPRE')


