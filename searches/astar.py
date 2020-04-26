from tools import estrutura_dados as No


def aestrela(mapa, inicio, fim):
    aberto = []
    fechado = []

    inicio_no = No.No(inicio, None)
    objetivo_no = No.No(fim, None)

    aberto.append(inicio_no)

    while len(aberto) > 0:
        aberto.sort()
        current_no = aberto.pop(0)
        fechado.append(current_no)
        if current_no == objetivo_no:
            path = []
            while current_no != inicio_no:
                path.append(current_no.posicao)
                current_no = current_no.pai
            return path[::-1]

        (x, y) = current_no.posicao
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        for next in neighbors:
            mapa_valor = mapa.get(next)
            if ((mapa_valor == '#') or (mapa_valor == '&')):
                continue
            neighbor = No.No(next, current_no)

            if (neighbor in fechado):
                continue
            neighbor.g = abs(neighbor.posicao[0] - inicio_no.posicao[0]) + abs(
                neighbor.posicao[1] - inicio_no.posicao[1])
            neighbor.h = abs(neighbor.posicao[0] - objetivo_no.posicao[0]) + abs(
                neighbor.posicao[1] - objetivo_no.posicao[1])
            neighbor.f = neighbor.g + neighbor.h
            for no in aberto:
                if (neighbor == no and neighbor.f > no.f):
                    continue
            aberto.append(neighbor)

    return None