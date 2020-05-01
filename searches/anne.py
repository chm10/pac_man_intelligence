import numpy as np
from tools.estrutura_dados import No

def simulated_annealing(mapa, inicio, fim, T0=1000, M=300, N=15, alpha=0.85, k=1):
    for i in range(M):  # usado para diminuir temperatura / passos
        for j in range(N):  # Quantas procuras fazer pelo vizinho
            # alpha = fator para decrementar temperatura quanto mais proximo menos movemos
            # T0 = Temperatura quão próximo devemo estar
            # k = fator do passo
            # random para escolher se vamos andar em x ou y depois ver qual sentido para baixo cima ou para direita ou esquerda
            rand_amp = np.random.rand()
            choose_x_y = np.random.rand()
            current = No(inicio, None)

            if choose_x_y >= 0.5:
                step_x = k * (1 if rand_amp < 0.5 else -1)
            else:
                step_y = -k * (1 if rand_amp < 0.5 else -1)

            x_temporary = x + step_x
            y_temporary = y + step_y

            (goal_x,goal_y) = current.posicao

            ## Escolhido calculamos o funcao objetivo ** Ideal era coloca multiplicador para penalizar se estamos proximos de fantasma
            obj_mov_possible = (x_temporary - goal_x) ** 2 + (y_temporary - goal_y) ** 2

            obj_val_current = (x_temporary - x) ** 2 + (y_temporary - y) ** 2

            ## fator de indecisao
            rand_factor = np.random.rand()

            ## equacao para determinar se estamos perto ou longe do objetivo
            probality_eq = 1 / (np.exp((obj_mov_possible - obj_val_current) / T0))

            if obj_mov_possible <= obj_val_current:  ## Como estamos mais proximo damos o passo
                x = x_temporary
                y = y_temporary
            elif rand_factor <= probality_eq:  ## deixa probalidade decidir
                x = x_temporary
                y = y_temporary
            else:  ## Nao vale a pena
                x = x
                y = y

            T0 = alpha * T0  ## Penaliza a temperatura

            ## Continua algoritmo...