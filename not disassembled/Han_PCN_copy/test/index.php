<?php

 if (isset($_GET["params"]) && isset($_GET["params1"]) && isset($_GET["params2_1"]) && isset($_GET["params2_2"])
	 && isset($_GET["params2_3"]) && isset($_GET["params2_4"])) 
    { echo " Получены новые вводные: данные датчика ESP - ".$_GET["params"].", ".$_GET["params1"].", ".$_GET["params2_1"].
     ", ".$_GET["params2_2"].", ".$_GET["params2_3"].", ".$_GET["params2_4"];} 
 else { echo "Переменные не дошли. Проверьте все еще раз."; }
$str = $_GET["params"];
$str1 = $_GET["params1"];
$str2 = $_GET["params2_1"];
$str3 = $_GET["params2_2"];
$str4 = $_GET["params2_3"];
$str5 = $_GET["params2_4"];
$myFile = "doc/hello.html";
$fd = fopen($myFile, 'w') or die("не удалось создать файл");
fwrite($fd, $str. "," . $str1. "," . $str2. "," . $str3. "," . $str4. "," . $str5);
fclose($fd);
$fd1 = fopen("doc/hello.txt", 'w+') or die("не удалось создать файл");
fwrite($fd1, $str. "\r\n" . $str1. "\r\n" . $str2. "\r\n" . $str3. "\r\n" . $str4. "\r\n" . $str5);
fclose($fd1);
?>