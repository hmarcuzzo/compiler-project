{Erro: índice de array 'c' não inteiro}
{Aviso: Variável 'a' declarada e não utilizada}
{Aviso: Variável 'b' declarada e não utilizada}
{Erro: Função principal deveria retornar inteiro, mas retorna vazio}

inteiro: a
flutuante: b
inteiro: c[1.2]

flutuante teste(inteiro: h, inteiro: f)
  inteiro: b
  h := f + 1
  retorna(teste(h, b) + h)
  escreva(teste() + h)
fim

inteiro principal()
  inteiro: a
  teste(a, a)
  c[5.8] := teste(a, b) + a
fim
