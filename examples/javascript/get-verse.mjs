const token = process.env.BIBLIA_API_TOKEN;

if (!token) {
  console.error("Defina BIBLIA_API_TOKEN antes de executar.");
  process.exit(1);
}

const url =
  "https://bibliaapi.com.br/api/v2/versions/acf/books/jo/chapters/3/verses/16";

const response = await fetch(url, {
  headers: {
    Accept: "application/json",
    Authorization: `Bearer ${token}`,
  },
  signal: AbortSignal.timeout(10_000),
});

const body = await response.json();

if (!response.ok) {
  console.error(`A API respondeu com ${response.status}.`, body);
  process.exit(1);
}

console.log(JSON.stringify(body, null, 2));
