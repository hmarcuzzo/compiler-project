import ply.lex as lex

from ply.lex import TOKEN


class tppLex():

    # Variáveis
    digito = r"([0-9])"
    letra = r"([a-zA-ZáÁãÃàÀéÉíÍóÓõÕ])"
    sinal = r"([\-\+]?)"
    
    # Tokens e simblos da linguagens
    tokens = [
        "ID",  # identificador
        # numerais
        "NUM_NOTACAO_CIENTIFICA",  # ponto flutuante em notaçao científica
        "NUM_PONTO_FLUTUANTE",  # ponto flutuate
        "NUM_INTEIRO",  # inteiro

        # operadores binarios
        "ADICAO",  # +
        "SUBTRACAO",  # -
        "MULTIPLICACAO",  # *
        "DIVISAO",  # /
        "E_LOGICO",  # &&
        "OU_LOGICO",  # ||
        "DIFERENCA",  # <>
        "MENOR_IGUAL",  # <=
        "MAIOR_IGUAL",  # >=
        "MENOR",  # <
        "MAIOR",  # >
        "IGUALDADE",  # =

        # operadores unarios
        "NEGACAO",  # !

        # simbolos
        "ABRE_PAR",  # (
        "FECHA_PAR",  # )
        "ABRE_COL",  # [
        "FECHA_COL",  # ]
        "VIRGULA",  # ,
        "DOIS_PONTOS",  # :
        "ATRIBUICAO",  # :=
        # 'COMENTARIO', # {***}
    ]

    # Plavras reservadas da linguagens
    reserved_words = {
        "se": "SE",
        "então": "ENTAO",
        "senão": "SENAO",
        "fim": "FIM",
        "repita": "REPITA",
        "flutuante": "FLUTUANTE",
        "retorna": "RETORNA",
        "até": "ATE",
        "leia": "LEIA",
        "escreva": "ESCREVA",
        "inteiro": "INTEIRO",
    }

    tokens = tokens + list(reserved_words.values())

    # Expressões Regulares para tokens simples:
    # Símbolos.
    t_ADICAO = r'\+'
    t_SUBTRACAO = r'-'
    t_MULTIPLICACAO = r'\*'
    t_DIVISAO = r'/'
    t_ABRE_PAR = r'\('
    t_FECHA_PAR = r'\)'
    t_ABRE_COL = r'\['
    t_FECHA_COL = r'\]'
    t_VIRGULA = r','
    t_ATRIBUICAO = r':='
    t_DOIS_PONTOS = r':'

    # Operadores Lógicos.
    t_E_LOGICO = r'&&'
    t_OU_LOGICO = r'\|\|'
    t_NEGACAO = r'!'

    # Operadores Relacionais.
    t_DIFERENCA = r'<>'
    t_MENOR_IGUAL = r'<='
    t_MAIOR_IGUAL = r'>='
    t_MENOR = r'<'
    t_MAIOR = r'>'
    t_IGUALDADE = r'='
    
    # Outras Expressões Regulares
    id = (
        r"(" + letra + r"(" + digito + r"+|_|" + letra + r")*)"
    )  # o mesmo que '((letra)(letra|_|([0-9]))*)'

    def t_COMENTARIO(self,token):
        r"(\{((.|\n)*?)\})"
        token.lexer.lineno += token.value.count("\n")

    @TOKEN(id)
    def t_ID(self,token):
        token.type = self.reserved_words.get(
            token.value, "ID"
        )  # não é necessário fazer regras/regex para cada palavra reservada
        # se o token não for uma palavra reservada automaticamente é um id
        # As palavras reservadas têm precedências sobre os ids

        return token

    def t_NUM_NOTACAO_CIENTIFICA(self,token):
        r"([+-]?[\d].[\d]+[eE][+-]?[\d]+)|([+-]?[\d][eE][+-]?[\d]+)"
        # token.value = float(token.value)    
        return token

    def t_NUM_PONTO_FLUTUANTE(self,token):
        r"[+-]?[\d].[\d]"
        # token.value = float(token.value)    
        return token

    def t_NUM_INTEIRO(self,token):
        r"[+-]?[\d]+"
        # token.value = int(token.value)    
        return token

    # Regra para contar o número de linhas 
    def t_newline(self,token):
        r'\n+'
        token.lexer.lineno += len(token.value)

    # Ignorar os espaços e tabs
    t_ignore  = ' \t'

    # Tratamento de erro
    def t_error(self,token):
        print("Caractere inválido '%s'" % token.value[0])

    # Build the lexer.
    def build(self,**kwargs):
        return lex.lex(module=self, **kwargs)