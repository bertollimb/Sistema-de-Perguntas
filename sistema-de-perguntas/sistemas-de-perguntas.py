perguntas = [
    {
        'Pergunta': 'Quanto é 2+2? ',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5? ',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2? ',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
] 
cont = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta.get('Pergunta'))
    print()
    for i, opcao in enumerate(pergunta.get('Opções')):
        print(f'{i}) {opcao}')
    indice_resposta = pergunta.get('Opções').index(pergunta.get('Resposta'))
    print()

    escolha = int(input('Escolha uma opção: '))
    if escolha == indice_resposta:
        cont += 1
        print('\033[32mAcertou\033[m ✅')
    else:
        print('\033[31mERROU\033[m ❌')

print(f'Você acertou {cont}')
print('de', len(perguntas), 'perguntas.')




       



        






