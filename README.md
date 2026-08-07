# BIBLIAAPI Examples

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
- [Status da plataforma](https://bibliaapi.com.br/status)

## Segurança

Nunca inclua uma chave real em código, commits, screenshots ou issues. Use variáveis de ambiente e consulte [`SECURITY.md`](SECURITY.md).

## Contribuindo

Exemplos para outras linguagens e frameworks são bem-vindos. Leia [`CONTRIBUTING.md`](CONTRIBUTING.md) antes de abrir um pull request.

## Licença

[MIT](LICENSE). A licença cobre somente os exemplos deste repositório; dados e serviços consumidos seguem os termos da BIBLIAAPI.
