# Análisador Léxico TPP

Análisador léxico da linguagem fictícia TPP.

## Configurações

### Requisitos
Certifique-se de ter instalado em sua máquina:

* Python >= 3.8 
* Python Lex Yacc >= 3.11.0

### Como Executar

Dentro da pasta ***impl*** execute:

```
python3 lex_submit.py code.tpp
```

ou 

```
python3 lex_submit.py code.tpp detailed
```

* ***code.tpp***: código tpp que será submetido para análise léxica.
* ***detailed***: parâmetro opcional, caso queira a saída mais detalahada (saída padrão do PLY)


Note que na pasta ```~/impl/testes_lexico/``` existem alguns arquivos ```.tpp``` para submeter ao código como exemplos.

