# BIBLIAAPI Examples

[![Quality](https://github.com/asllanmaciel/bibliaapi-examples/actions/workflows/quality.yml/badge.svg)](https://github.com/asllanmaciel/bibliaapi-examples/actions/workflows/quality.yml)
[![Release](https://img.shields.io/github/v/release/asllanmaciel/bibliaapi-examples?display_name=tag&sort=semver)](https://github.com/asllanmaciel/bibliaapi-examples/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-0f766e.svg)](LICENSE)

Exemplos pequenos e seguros para integrar aplicações à [BIBLIAAPI](https://bibliaapi.com.br), uma API bíblica em português com contrato OpenAPI.

Este repositório contém somente clientes de exemplo. O código da plataforma, autenticação, cobrança e infraestrutura permanece privado.

## Comece em três passos

1. Crie uma conta gratuita em [bibliaapi.com.br/conta](https://bibliaapi.com.br/conta).
2. Gere uma chave de API no painel.
3. Exporte a chave antes de executar um exemplo:

```bash
export BIBLIA_API_TOKEN="sua_chave"
```

No PowerShell:

```powershell
$env:BIBLIA_API_TOKEN = "sua_chave"
```

## Exemplos disponíveis

| Linguagem | Arquivo | Execução |
|---|---|---|
| cURL | [`examples/curl/get-verse.sh`](examples/curl/get-verse.sh) | `bash examples/curl/get-verse.sh` |
| PHP | [`examples/php/get-verse.php`](examples/php/get-verse.php) | `php examples/php/get-verse.php` |
| JavaScript | [`examples/javascript/get-verse.mjs`](examples/javascript/get-verse.mjs) | `node examples/javascript/get-verse.mjs` |

Todos consultam João 3:16 na versão ACF usando:

```text
GET /api/v2/versions/acf/books/jo/chapters/3/verses/16
Authorization: Bearer SUA_CHAVE
```

## Recursos

- [Guia de integração](https://bibliaapi.com.br/integrar)
- [Contrato OpenAPI](https://bibliaapi.com.br/api/v2/openapi.yaml)

## Segurança

Nunca inclua uma chave real em código, commits, screenshots ou issues. Use variáveis de ambiente e consulte a [política de segurança](.github/SECURITY.md).

## Contribuindo

Exemplos para outras linguagens e frameworks são bem-vindos. Leia o [guia de contribuição](CONTRIBUTING.md) e o [código de conduta](CODE_OF_CONDUCT.md) antes de abrir um pull request.

- [Escolha uma tarefa para primeira contribuição](https://github.com/asllanmaciel/bibliaapi-examples/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22)
- [Veja todas as tarefas que precisam de ajuda](https://github.com/asllanmaciel/bibliaapi-examples/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22help%20wanted%22)

## Licença

[MIT](LICENSE). A licença cobre somente os exemplos deste repositório; dados e serviços consumidos seguem os termos da BIBLIAAPI.
