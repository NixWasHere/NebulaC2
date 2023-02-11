<?php
 $SS = $_GET['SQL_USER'];
 $files_main = fopen("mysql_db_user.txt",'a');
 fwrite($files_main,$SS."". PHP_EOL);
 fclose($files_main);
?>
