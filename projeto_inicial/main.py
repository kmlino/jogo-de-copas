import random

# IMPRIME O TABULEIRO
def imprime_tabuleiro(cartas_p1, cartas_p2):
    s = '''
    {0} | {1} | {2} | {3} | {4}
    --------------------------
         {10}    |    {11}
    --------------------------
    {5} | {6} | {7} | {8} | {9}
    '''
    t = cartas_p1 + cartas_p2
    t.append(' ')
    t.append(' ')
    print(s.format(*t))

# IMPRIME O TABULEIRO ATUALIZADO
def imprime_restante(cartas_p1, cartas_p2, jogada_p1, jogada_p2):
    s = '''
    {0} | {1} | {2} | {3} | {4}
    --------------------------
         {10}    |    {11}
    --------------------------
    {5} | {6} | {7} | {8} | {9}
    '''
    t = cartas_p1 + cartas_p2
    t.append(jogada_p1 if jogada_p1 else ' ')
    t.append(jogada_p2 if jogada_p2 else ' ')
    print(s.format(*t))

# EMBARALHA O BARALHO E RETORNA 12 CARTAS ALEATÓRIAS
def embaralha(baralho):
    random.shuffle(baralho)
    rdm = [i for i in baralho]
    return rdm[:12]

# DISTRIBUI AS CARTAS EM ORDEM CRESCENTE
def distribui_cartas(baralho):
    val = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    val_inv = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}
    lista_ordenada = []
    resultado = []

    for i in baralho:
        num = val[i[1:]] if i[1:] in val else int(i[1:])
        lista_ordenada.append((num, i[0]))
    for j in sorted(lista_ordenada):
        char = val_inv[j[0]] if j[0] in val_inv else str(j[0])
        resultado.append(j[-1] + char)

    return resultado

# VERIFICA O VENCEDOR DE CADA RODADA
def verifica_vencedor_rodada(carta_p1, carta_p2, naipe):
    val = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    p1 = int(carta_p1[1:]) if carta_p1[1:] not in val else val[carta_p1[1:]]
    p2 = int(carta_p2[1:]) if carta_p2[1:] not in val else val[carta_p2[1:]]

    if carta_p1[0] == carta_p2[0]:
        return True if p1 > p2 else False
    elif carta_p1[0] != carta_p2[0]:
        return True if naipe == carta_p1[0] else False

# VERIFICA O VENCEDOR DA PARTIDA, O PRIMEIRO JOGADOR QUE ATINGIR 3 VITÓRIAS
def verifica_vencedor_partida(cartas_p1, cartas_p2, win_p1, win_p2):
    if (cartas_p1.count(None) >= 5 and cartas_p2.count(None) >= 5) or (win_p1 >= 3 or win_p2 >= 3):
        print('Vencedor da partida: Jogador 1!!!' if win_p1 > win_p2 else 'Vencedor da partida: Jogador 2!!!')
    else:
        pass

# HUMANO REALIZA JOGADAS
def joga_humano(cartas):
    jogada = input('Escolha uma carta: ').upper()
    while jogada not in cartas:
        jogada = input('Carta inválida, tente novamente: ').upper()
    return jogada

# A MÁQUINA REALIZA JOGADAS
def joga_cpu(cartas, jogada_adv):
    c = cartas.copy()
    val = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    equal = []
    diff = []
    for k, v in val.items():
        for i in c:
            if i is not None:
                if i[1:] == k:
                    c[c.index(i)] = i[0] + str(v)

    naipe = [x[0] if x is not None else None for x in c]

    for x in c:
        if x is not None:
            if x[0] == jogada_adv[0]:
                equal.append([x[0], int(x[1:])])
            else:
                diff.append([x[0], int(x[1:])])

    res = max(equal) if jogada_adv[0] in naipe else min(diff)
    st = res[0]
    it = str(res[1])
    for k, y in val.items():
        if it == str(y):
            it = k
    return st + it

# INICIALIZAÇÃO E EXECUÇÃO DO JOGO
naipes = ['C', 'E', 'O', 'P']
valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
baralho = [(x+y) for x in naipes for y in valores]
tabuleiro = embaralha(baralho)
cartas_jogador_um = distribui_cartas(tabuleiro[:5])
cartas_jogador_dois = distribui_cartas(tabuleiro[5:10])
vencedor1 = 0
vencedor2 = 0
vencedor_atual = 0
naipe_da_vez = ''

imprime_tabuleiro(cartas_jogador_um, cartas_jogador_dois)

while vencedor1 < 3 and vencedor2 < 3:
    if vencedor_atual == 1:
        print('Jogador 1, sua vez!')
        jogada_p1 = joga_humano(cartas_jogador_um)
        naipe_da_vez = jogada_p1[0]
        cartas_jogador_um[cartas_jogador_um.index(jogada_p1)] = None
        print('Carta da vez: {0}'.format(jogada_p1))
        print('Jogador 2, sua vez!')
        jogada_p2 = joga_cpu(cartas_jogador_dois, jogada_p1)
        cartas_jogador_dois[cartas_jogador_dois.index(jogada_p2)] = None

    elif vencedor_atual == 2:
        print('Jogador 2, sua vez!')
        jogada_p2 = joga_cpu(cartas_jogador_dois, jogada_p1)
        naipe_da_vez = jogada_p2[0]
        cartas_jogador_dois[cartas_jogador_dois.index(jogada_p2)] = None
        print('Carta da vez: {0}'.format(jogada_p2))
        print('Jogador 1, sua vez!')
        jogada_p1 = joga_humano(cartas_jogador_um)
        cartas_jogador_um[cartas_jogador_um.index(jogada_p1)] = None

    else:
        print('Jogador 1, sua vez!')
        jogada_p1 = joga_humano(cartas_jogador_um)
        naipe_da_vez = jogada_p1[0]
        cartas_jogador_um[cartas_jogador_um.index(jogada_p1)] = None
        print('Carta da vez: {0}'.format(jogada_p1))
        print('Jogador 2, sua vez!')
        jogada_p2 = joga_cpu(cartas_jogador_dois, jogada_p1)
        cartas_jogador_dois[cartas_jogador_dois.index(jogada_p2)] = None

    print('\n')
    imprime_restante(cartas_jogador_um, cartas_jogador_dois, jogada_p1, jogada_p2)

    if verifica_vencedor_rodada(jogada_p1, jogada_p2, naipe_da_vez):
        vencedor1 += 1
        vencedor_atual = 1
        print('Vencedor da rodada: Jogador 1!')
    else:
        vencedor2 += 1
        vencedor_atual = 2
        print('Vencedor da rodada: Jogador 2!')

    print('Placar: Jogador 1= {0}  |  Jogador 2= {1}'.format(vencedor1, vencedor2))
    verifica_vencedor_partida(cartas_jogador_um, cartas_jogador_dois, vencedor1, vencedor2)
