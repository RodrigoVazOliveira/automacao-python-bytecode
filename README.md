## ByteBank

---

para criar novo ambiente virtual

```bash
$ python3 -m venv venv
```

Para ativar o ambiente

```bash
$ source venv/bin/activate
```

cobertura de teste:

```bash
$ pytest --cov=src  tests/
```

Para ver as linhas faltantes:

```bash
$ pytest --cov=src  tests/ --cov-report term-missing
```

Gerando relatório em HTML
```bash
$ pytest --cov=src  tests/ --cov-report html
```

gerar um relatorio em xml
```bash 
$ pytest --junitxml report.xml or 
$ pytest --cov-report xml
```