const token = process.env.BIBLIA_API_TOKEN;

if (!token) {
  console.error("Defina BIBLIA_API_TOKEN antes de executar.");
  process.exit(1);
}

const url =
  "https://bibliaapi.com.br/api/v2/versions/acf/books/jo/chapters/3/verses/16";

let response;

try {
  response = await fetch(url, {
    headers: {
      Accept: "application/json",
      Authorization: `Bearer ${token}`,
    },
    signal: AbortSignal.timeout(10_000),
  });
} catch (error) {
  const message = error instanceof Error ? error.message : String(error);
  console.error(`Não foi possível conectar à BIBLIAAPI: ${message}`);
  process.exit(1);
}

const rawBody = await response.text();
let body;

try {
  body = rawBody === "" ? null : JSON.parse(rawBody);
} catch (error) {
  if (!response.ok) {
    console.error(`A API respondeu com ${response.status}.`, rawBody);
  } else {
    const message = error instanceof Error ? error.message : String(error);
    console.error(`A API respondeu com JSON inválido: ${message}`);
  }
  process.exit(1);
}

if (!response.ok) {
  console.error(`A API respondeu com ${response.status}.`, body);
  process.exit(1);
}

console.log(JSON.stringify(body, null, 2));
