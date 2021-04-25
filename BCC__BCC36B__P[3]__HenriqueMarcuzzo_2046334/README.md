# Análisador Semântico TPP

Análisador semântico da linguagem fictícia TPP.

## Configurações

### Requisitos
Certifique-se de ter instalado em sua máquina:

* Python >= 3.8 
* Python Lex Yacc >= 3.11.0
* Python Graphviz

### Como Executar

Dentro do diretório ```impl``` execute:

```
python3 tppSintatic.py code.tpp
```

* ```code.tpp```: código tpp que será submetido para análise sintática.

Note que na pasta ```~/impl/sintatica-testes/``` existem alguns arquivos ```.tpp``` para submeter ao código como exemplos.

O código ira gerar a árvore do código submetido se este não conter nenhum erro sintático.
