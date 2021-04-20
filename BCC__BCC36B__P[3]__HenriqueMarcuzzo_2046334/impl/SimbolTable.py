class SimbolTable():
    def __init__(self, token, lexema, tipo, dim, tam_dim1, tam_dim2, escopo, init, linha):
        self.token = token
        self.lexema = lexema
        self.tipo = tipo
        self.dim = dim
        self.tam_dim1 = tam_dim1
        self.tam_dim2 = tam_dim2
        self.escopo = escopo
        self.init = init
        self.linha = linha