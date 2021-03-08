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

    if len(argv) > 2 and argv[2] == 'detailed':
        print_mode = argv[2]
    else:
        print_mode = 'simple'

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input

        if print_mode == 'detailed':
            print(tok)
        else:
            print(tok.type)


if __name__ == "__main__":
    main()