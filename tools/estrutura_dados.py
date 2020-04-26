class No:
    def __init__(self, posicao: (), pai: ()):
        self.posicao = posicao
        self.pai = pai
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, outro):
        return self.posicao == outro.posicao

    def __lt__(self, outro):
        return self.f < outro.f

    def __repr__(self):
        return ('({0},{1})'.format(self.posicao, self.f))
