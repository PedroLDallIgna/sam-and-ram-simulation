# Comparativo entre SAM e RAM

## Alunos
* Henrique Bonatto
* Pedro Lucas Dall' Igna

## Como utilizar
Os script está dentro de `app.py`. O arquivo para leitura é passado como argumento de linha de comando para `app.py`.
```
(python | py3 | python3) app.py path/to/file.txt
```

Depois de aberto, haverá um loop para input de comandos. Os comandos disponíveis são:
- `search [word]`: será executada a pesquisa pelo argumento `word` dentro da memória, mostrando os resultados em milissegundos. O argumento `word` junto com `search` é opcional. Se for digitado apenas `search`, haverá um novo input para determinar a `word`.
- `quit`: sairá do programa.
- `help`: mostrará a ajuda do programa, mostrando os comandos disponíveis como exemplificado aqui.
