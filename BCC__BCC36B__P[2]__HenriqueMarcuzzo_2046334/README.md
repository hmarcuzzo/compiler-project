# Análisador Sintatico TPP

Análisador sintatico da linguagem fictícia TPP.

## Configurações

### Requisitos
Certifique-se de ter instalado em sua máquina:

* Python >= 3.8 
* Python Lex Yacc >= 3.11.0
* Python Graphviz >= 0.16

### Como Executar

Dentro do diretório ```impl``` execute:

```
python3 tppSemantic.py code.tpp
```

* ```code.tpp```: código tpp que será submetido para análise semântica.

Note que na pasta ```~/impl/semantica-testes/``` existem alguns arquivos ```.tpp``` para submeter ao código como exemplos.

O código ira gerar a árvore do código submetido se este não conter nenhum erro sintático, uma tabela de símbolos para as
funções e outra para as váriaves, irá mostrar também todas as mensagens de aviso e erro semântico, como também irá gerar
uma árvore simplificada (o destino também será mostrado no terminal).
