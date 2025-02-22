<?php

function connectToDatabase() : mysqli {

    if($_ENV['ENV'] == 'DEV'){
        $host = $_ENV['DB_DEV_HOST'];
        $user = $_ENV['DB_DEV_USER'];
        $password = $_ENV['DB_DEV_PASSWORD'];
        $database = $_ENV['DB_DEV_NAME'];
    } else {
        $host = $_ENV['DB_PROD_HOST'];
        $user = $_ENV['DB_PROD_USER'];
        $password = $_ENV['DB_PROD_PASSWORD'];
        $database = $_ENV['DB_PROD_NAME'];
    }

    $conn = new mysqli($host, $user, $password, $database);

    $conn->set_charset("utf8mb4");

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    return $conn;
}

function getGuzzleClient() : \GuzzleHttp\Client {

    return new \GuzzleHttp\Client();
}

function getMailer() : \PHPMailer\PHPMailer\PHPMailer {

    $mail = new \PHPMailer\PHPMailer\PHPMailer(true);
    $mail->isSMTP();
    $mail->Host = $_ENV['MAIL_HOST'];
    $mail->SMTPAuth = true;
    $mail->Username = $_ENV['MAIL_USERNAME'];
    $mail->Password = $_ENV['MAIL_PASSWORD'];
    $mail->SMTPSecure = \PHPMailer\PHPMailer\PHPMailer::ENCRYPTION_STARTTLS;
    $mail->Port = $_ENV['MAIL_PORT'];
    return $mail;
}

function getTwig(string $templatePath = 'templates'): \Twig\Environment
{
    $loader = new \Twig\Loader\FilesystemLoader($templatePath);
    $twig = new \Twig\Environment($loader);
    return $twig;
}

function getAssetFunction(int $depth = 0): \Twig\TwigFunction
{
    $baseUrl = rtrim(dirname($_SERVER['SCRIPT_NAME']), '/');
    for ($i = 0; $i < $depth; $i++) {
        $baseUrl = rtrim(dirname($baseUrl), '/');
    }

    return new \Twig\TwigFunction('asset', function ($path) use ($baseUrl) {
        return $baseUrl . '/' . ltrim($path, '/');
    });
}

function getURLFunction(int $depth = 0): \Twig\TwigFunction
{
    $baseUrl = rtrim(dirname($_SERVER['SCRIPT_NAME']), '/');
    for ($i = 0; $i < $depth; $i++) {
        $baseUrl = rtrim(dirname($baseUrl), '/');
    }

    return new \Twig\TwigFunction('url', function ($path) use ($baseUrl) {
        return $baseUrl . '/' . ltrim($path, '/');
    });
}

function getRecaptchaSiteKey() : string {
    if($_ENV['ENV'] == 'PROD') {
        return $_ENV['RECAPTCHA_KEY_REQUEST_PROD'];
    } else {
        return $_ENV['RECAPTCHA_KEY_REQUEST'];
    }
}

function getRecaptchaSecretKey() : string {
    if($_ENV['ENV'] == 'PROD') {
        return $_ENV['RECAPTCHA_KEY_RESPONSE_PROD'];
    } else {
        return $_ENV['RECAPTCHA_KEY_RESPONSE'];
    }
}

function url(string $path = '') : string {
    return rtrim($_ENV['URL_BASE'], '/') . '/' . ltrim($path, '/');
}

function generateToken() : string {
    return bin2hex(random_bytes(32));
}
