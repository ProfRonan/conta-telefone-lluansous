# Especificação do exercício

Escreva um script que calcula a conta de telefone mensal seguindo as seguintes regras:

- Mínimo de R$ 200,00 até um máximo de 100 ligações.
- Mais R$ 0,60 por ligação para as próximas 50 ligações.
- Mais R$ 0,50 por ligação para as próximas 50 ligações.
- Mais R$ 0,40 por ligação a partir da 201ª ligação.

O programa deve pedir o número de ligações que o usuário fez ao longo do mês e exibir como saída a seguinte mensagem:

```markdown
O valor devido é R$ [Valor com duas casas decimais].
```

Substituindo os colchetes pelo valor correto.

## Exemplos

Se o usuário fizer 101 ligações o programa deve responder:

```markdown
O valor devido é R$ 200.60.
```

Se o usuário fizer 151 ligações o programa deve responder:

```markdown
O valor devido é R$ 230.50.
```
