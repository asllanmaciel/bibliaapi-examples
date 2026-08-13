# Clientes resilientes para APIs HTTP

Os exemplos deste repositório são pequenos de propósito. Em aplicações reais, uma chamada HTTP precisa tratar mais do que o caminho de sucesso.

Este guia descreve um baseline independente de linguagem para consumir a BIBLIAAPI — e APIs HTTP em geral — sem transformar falhas transitórias em travamentos, loops de retry ou vazamento de credenciais.

## 1. Token fora do código

Mantenha credenciais em variáveis de ambiente ou em um secret manager apropriado ao ambiente de execução.

Evite:

- commitar tokens em arquivos de configuração;
- inserir tokens em URLs;
- imprimir o header `Authorization` em logs;
- copiar credenciais reais para screenshots, issues ou fixtures.

Falhe de forma explícita quando a credencial obrigatória não estiver disponível.

## 2. Timeout é obrigatório

Uma requisição sem limite de tempo pode prender uma thread, processo PHP, worker ou execução serverless indefinidamente.

Defina pelo menos:

- **connection timeout**: quanto esperar para estabelecer conexão;
- **request/read timeout**: quanto esperar pela resposta completa.

Os valores dependem do produto e do ambiente. O objetivo é ter um limite deliberado, não um número universal.

## 3. Separe transporte, HTTP e payload

Existem pelo menos três classes diferentes de falha:

```text
transporte
  DNS, TLS, conexão, timeout

HTTP
  resposta recebida, mas status não representa sucesso

payload
  status pode até ser 2xx, mas o corpo não tem o formato esperado
```

Não trate essas três situações como a mesma exceção genérica. A distinção ajuda observabilidade, retry e diagnóstico.

## 4. Não assuma que toda resposta é JSON

Mesmo quando a API normalmente responde JSON, proxies, gateways, erros de infraestrutura e páginas intermediárias podem produzir outro conteúdo.

Uma estratégia segura é:

1. receber a resposta;
2. registrar status e metadata mínima;
3. tentar decodificar JSON;
4. tratar parsing inválido como erro próprio;
5. nunca assumir campos antes de validar a estrutura necessária.

Evite registrar o corpo inteiro automaticamente quando ele puder conter dados sensíveis.

## 5. HTTP não-2xx precisa de política explícita

Não siga adiante com lógica de negócio quando a resposta HTTP indica falha.

Classifique os erros conforme o comportamento da aplicação. Exemplos comuns:

- falha de autenticação/autorização: normalmente exige corrigir credencial/configuração, não retry imediato;
- recurso/parâmetro inválido: normalmente exige corrigir a requisição;
- limitação temporária: pode permitir retry controlado;
- falha de servidor/rede: pode ser transitória, mas retry precisa ser limitado.

A aplicação deve consultar o contrato/documentação atual da API para interpretar códigos e campos específicos.

## 6. Retry somente quando fizer sentido

Retry automático em toda falha pode piorar uma indisponibilidade ou repetir uma requisição inválida milhares de vezes.

Quando retry for apropriado:

- limite o número de tentativas;
- use atraso crescente/backoff;
- adicione jitter quando muitos workers possam falhar simultaneamente;
- respeite orientação do servidor quando houver informação de retry;
- não faça retry infinito dentro da requisição do usuário.

Para operações com efeitos colaterais, idempotência deve ser considerada antes de qualquer retry. Os exemplos atuais deste repositório usam leitura (`GET`), mas clientes futuros podem ter requisitos diferentes.

## 7. Logue o suficiente, não o segredo

Uma linha útil para investigação pode conter:

```text
operation=get_verse
http_status=...
duration_ms=...
attempt=...
error_category=transport|http|payload
request_id=...
```

Não inclua:

```text
Authorization: Bearer <token>
```

Se a API retornar um identificador de request/correlation, preserve-o para suporte e investigação sem armazenar credenciais.

## 8. Valide o contrato usado pela aplicação

Decodificar JSON com sucesso não prova que o payload tem os campos necessários.

Para um cliente de produção, valide pelo menos a parte do contrato que a aplicação consome. Dependendo da linguagem, isso pode ser feito com:

- DTOs e validação explícita;
- schemas;
- tipos gerados a partir de OpenAPI;
- validação manual pequena para exemplos simples.

Evite propagar arrays/objetos HTTP crus por toda a aplicação quando somente alguns campos são necessários.

## 9. Não misture cliente HTTP com regra de negócio

Uma fronteira simples deixa o código mais testável:

```text
Controller / CLI / Job
        ↓
Application service
        ↓
BibleApiClient
        ↓
HTTP transport
```

Assim, testes de regra de negócio podem usar um cliente falso/in-memory sem depender de rede, token ou disponibilidade externa.

## 10. Checklist de produção

Antes de promover um exemplo para código de aplicação, revise:

- [ ] token fora do repositório;
- [ ] HTTPS;
- [ ] connection/request timeout;
- [ ] erro de transporte tratado;
- [ ] HTTP não-2xx tratado antes da regra de negócio;
- [ ] JSON inválido tratado;
- [ ] campos realmente consumidos validados;
- [ ] retry limitado e somente para falhas apropriadas;
- [ ] logs sem token/headers sensíveis;
- [ ] testes sem depender obrigatoriamente da API real;
- [ ] monitoramento de latência/falhas quando a integração for crítica.

Os exemplos do repositório servem como ponto de partida. Aplicações reais devem adaptar limites, retries, observabilidade e validação ao próprio risco operacional.