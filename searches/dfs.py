import estrutura_dados as No

def depth_first_search(mapa, inicio, fim):
    aberto = []
    fechado = []
    no_inicio = No.No(inicio, None)
    no_objetivo = No.No(fim, None)

    aberto.append(no_inicio)
    while len(aberto) > 0:
        no_atual = aberto.pop(-1)
        fechado.append(no_atual)
        if no_atual == no_objetivo:
            path = []
            while no_atual != no_inicio:
                path.append(no_atual.posicao)
                no_atual = no_atual.pai
            return path[::-1]

        (x, y) = no_atual.posicao
        vizinhos = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        for proximo in vizinhos:
            valor_mapa = mapa.get(proximo)
            if ((valor_mapa == '#') or (valor_mapa == '&')):
                continue

            vizinhos = No.No(proximo, no_atual)
            if (vizinhos in fechado):
                continue
            if (vizinhos not in aberto):
                aberto.append(vizinhos)
    return None