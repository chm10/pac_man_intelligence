from tools import estrutura_dados as No


def breadth_first_search(mapa, inicio, fim):
    aberto = []
    fechado = []

    inicio_node = No.No(inicio, None)
    objetivo = No.No(fim, None)

    aberto.append(inicio_node)

    while len(aberto) > 0:

        no_atual = aberto.pop(0)
        fechado.append(no_atual)

        if no_atual == objetivo:
            caminho = []
            while no_atual != inicio_node:
                caminho.append(no_atual.posicao)
                no_atual = no_atual.pai
            return caminho[::-1]

        (x, y) = no_atual.posicao

        vizinhos = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        for proximo in vizinhos:

            valor = mapa.get(proximo)

            if (valor == '#') or (valor == '&') or (valor == ' '):
                continue

            vizinho = No.No(proximo, no_atual)

            if (vizinho in fechado):
                continue

            if (vizinho not in aberto):
                aberto.append(vizinho)

    return None
