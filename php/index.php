<?php

declare(strict_types=1);

$request = $_SERVER['REQUEST_URI'];
$progLanguage = 'PHP';

switch ($request) {
    case '/':
        http_response_code(200);

        echo "<h1>Hello World from $progLanguage</h1>";

        break;
    case '/language':
        http_response_code(200);

        echo json_encode([
            'language' => $progLanguage,
        ]);

        break;
    default:
        http_response_code(404);

        break;
}
