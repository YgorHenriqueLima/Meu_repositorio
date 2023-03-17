<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Manipulação de string</title>
</head>
<body>
    <?php
        /*interpretando a variável */
       $nome = "Gustavo";
       $sobrenome = "Guanabara";
       echo "$nome$sobrenome \u{1F596}";
       /*echo '$nome$sobrenome \u{🖖🏻}'; sem interpretar*/
    ?>
</body>
</html>