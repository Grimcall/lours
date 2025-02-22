<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

function retrieveMailer(string $fromName = '') : PHPMailer {
    $email = $_ENV['EMAIL_USER'];
    $password = $_ENV['EMAIL_PASSWORD'];
    $host = $_ENV['EMAIL_HOST'];
    $port = $_ENV['EMAIL_PORT'];

    $mail = new PHPMailer(true);
    try {
        $mail->CharSet = 'UTF-8';
        $mail->isSMTP();
        $mail->Host = $host;
        $mail->SMTPAuth = true;
        $mail->Username = $email;
        $mail->Password = $password;
        $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
        $mail->Port = $port;

        $mail->setFrom($email, $fromName);
        $mail->isHTML(true);
        return $mail;
    } catch (Exception $e) {
        echo "Error al crear el objeto PHPMailer: " . $mail->ErrorInfo;
        return null;
    }
}

function sendMailStandard(string $selfEmail, string $to, string $subject, string $body, string $fromName = '') : void {
    try {
        // Send email to self.
        $mail = retrieveMailer($fromName);
        $mail->addAddress($selfEmail); 
        $mail->Subject = $subject;
        $mail->Body = $body;
        $mail->send();

        // Send email to the user
        if ($to !== $selfEmail && $to !== "") {
            $mail->clearAddresses();
            $mail->addAddress($to);
            $mail->send();
        }
    } catch (Exception $e) {
        echo "Error al enviar el correo: " . $mail->ErrorInfo;
    }
}