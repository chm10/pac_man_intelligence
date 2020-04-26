from tools import estrutura_dados as No


def best_first_search(mapa, inicio, fim):
    # Create lists for aberto nos and fechado nos
    aberto = []
    fechado = []

    # Create a inicio no and an goal no
    no_inicio = No.No(inicio, None)
    objetivo = No.No(fim, None)

    # Add the inicio no
    aberto.append(no_inicio)

    # Loop until the aberto list is empty
    while len(aberto) > 0:

        # Sort the aberto list to get the no with the lowest cost first
        aberto.sort()

        # Get the no with the lowest cost
        no_atual = aberto.pop(0)

        # Add the current no to the fechado list
        fechado.append(no_atual)

        # Check if we have reached the goal, return the path
        if no_atual == objetivo:
            path = []
            while no_atual != no_inicio:
                path.append(no_atual.posicao)
                no_atual = no_atual.pai
            # path.append(inicio) 
            # Return reversed path
            return path[::-1]

        # Unzip the current no posicao
        (x, y) = no_atual.posicao

        # Get vizinhos
        vizinhos = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        # Loop vizinhos
        for proximo in vizinhos:

            # Get value from mapa
            valor = mapa.get(proximo)

            # Check if the no is a wall
            if (valor == '#'):
                continue

            # Create a vizinho no
            vizinho = No.No(proximo, no_atual)

            # Check if the vizinho is in the fechado list
            if (vizinho in fechado):
                continue

            # Generate heuristics (Manhattan distance)
            vizinho.g = abs(vizinho.posicao[0] - no_inicio.posicao[0]) + abs(
                vizinho.posicao[1] - no_inicio.posicao[1])
            vizinho.h = abs(vizinho.posicao[0] - objetivo.posicao[0]) + abs(
                vizinho.posicao[1] - objetivo.posicao[1])
            vizinho.f = vizinho.h

            # Check if vizinho is in aberto list and if it has a lower f value
            for no in aberto:
                if (vizinho == no and vizinho.f > no.f):
                    continue

            # Everything is green, add vizinho to aberto list
            aberto.append(vizinho)

    # Return None, no path is found
    return None

# The main entry point for this module
