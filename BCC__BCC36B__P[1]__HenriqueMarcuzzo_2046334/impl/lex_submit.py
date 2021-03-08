import tppLex as lex

from sys import argv, exit

def main():
    aux = argv[1].split('.')
    if aux[-1] != 'tpp':
        raise IOError("Not a .tpp file!")
    data = open(argv[1])

    source_file = data.read()
    data.close()

    class_lexer = lex.tppLex()
    lexer = class_lexer.build()

    lexer.input(source_file)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
        # print(tok.type)
        # print(tok.value)

if __name__ == "__main__":
    main()