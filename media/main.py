from calc_media import CalculadoraDeMedia

while True:
    print('''
Opções:
0 - Calcular média
1 - Sair
    ''')
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 0:
        nota1 = int(input("Digite a nota 1: "))

        nota2 = int(input("Digite a nota 2: "))

        nota3 = int(input("Digite a nota 3: "))

        resultado = CalculadoraDeMedia.calcular(nota1, nota2, nota3)
        print('Resultado:', resultado)
    elif opcao == 1:
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")