<html>
<head>
    <meta http-equiv="refresh" content="300">
    <link href="static/stock.css" rel="stylesheet" type="text/css" />
</head>
<body>
<?php
    $url = "http://finance.yahoo.com/d/quotes.csv?s=TWLO+&f=sb3b2l1l";
    $content = file_get_contents($url);
    $pieces = explode(",", $content);
    echo "<div class='symbol'>TWLO";
                echo "<div class='stock-price'>";
                echo $pieces[3];
                echo "</div>";
        echo "</div>";
?>
</body>
</html>
