info_atleta = []

while True:
    name = str(input("Nome: "))
    if name == '':
        break
    else:
        info_atleta.append(name)
        for s in range(5):
            resp = float(input(f"Informe o salto {s+1}: "))
            info_atleta.append(resp)
        cont = 0
        for i in info_atleta[1:]:
            cont += 1
            print(f'Salto {cont}: ', i)
        print('\nResultado final: \n'
            f'Atleta: {info_atleta[0]}\n'
            f'Saltos: {info_atleta[1:]}\n'
            f'Média dos saltos: {sum(info_atleta[1:])/len(info_atleta[1:])} m')




