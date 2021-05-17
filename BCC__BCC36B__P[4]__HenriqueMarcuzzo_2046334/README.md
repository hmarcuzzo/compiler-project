# Gerador de Código TPP

Gerador de código executável da linguagem fictícia TPP.

## Configurações

### Requisitos
Certifique-se de ter instalado em sua máquina:

* Python >= 3.8 
* Python Lex Yacc >= 3.11.0
* clang >= 10.0.0
* Python Graphviz
* LLVM

### Como Executar

Dentro do diretório ```implementacao``` execute:

```
python3 tppGenerator.py code.tpp
```

* ```code.tpp```: código tpp que será submetido para análise sintática.

Note que na pasta ```~/implementacao/geracao-codigo-testes/``` existem alguns arquivos ```.tpp``` para submeter ao código como exemplos.

O código ira gerar um código ```.ll``` intermediário e um ```.o``` executável, caso queira executar o código compilado basta exeuta-lo.
