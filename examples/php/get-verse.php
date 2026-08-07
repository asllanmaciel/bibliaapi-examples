<?php

declare(strict_types=1);

$token = getenv('BIBLIA_API_TOKEN');

if ($token === false || $token === '') {
    fwrite(STDERR, "Defina BIBLIA_API_TOKEN antes de executar.\n");
    exit(1);
}

$url = 'https://bibliaapi.com.br/api/v2/versions/acf/books/jo/chapters/3/verses/16';
$context = stream_context_create([
    'http' => [
        'method' => 'GET',
        'header' => [
            'Accept: application/json',
            'Authorization: Bearer ' . $token,
        ],
        'ignore_errors' => true,
        'timeout' => 10,
    ],
]);

$response = file_get_contents($url, false, $context);

if ($response === false) {
    fwrite(STDERR, "Não foi possível conectar à BIBLIAAPI.\n");
    exit(1);
}

$statusLine = $http_response_header[0] ?? '';

if (!str_contains($statusLine, ' 200 ')) {
    fwrite(STDERR, "A API respondeu com erro: {$statusLine}\n{$response}\n");
    exit(1);
}

$data = json_decode($response, true, 512, JSON_THROW_ON_ERROR);
echo json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE) . PHP_EOL;
