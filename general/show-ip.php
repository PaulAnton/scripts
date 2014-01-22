<?php

$full = 1; # 0 = only show the IP, 1 = show other info
$ip = $_SERVER['REMOTE_ADDR'];

// A function to check if the header is present
function check_header($header) {
  if ($_SERVER[$header] != NULL) {
    return $_SERVER[$header];
  }else {
    return('None detected');
  }
}

if ($full == 0) {
  header('Your IP: '. $ip);
  echo $ip;

}else{
  header('Your IP: '. $ip);

  // Check for the HTTP_X_FORWARDED header
  $forwarded = check_header('HTTP_X_FORWARDED');
  header('HTTP_X_FORWARDED: '. $forwarded);

  // Check for the HTTP_X_FORWARDED_FOR header
  $forwarded_for = check_header('HTTP_X_FORWARDED_FOR');
  header('HTTP_X_FORWARDED_FOR: '. $forwarded_for);
  
  // Check for the HTTP_FORWARDED header
  $forwarded2 = check_header('HTTP_FORWARDED');
  header('HTTP_FORWARDED: '. $forwarded2);

  // Check for the FORWARDED header
  $forward = check_header('FORWARDED');
  header('FORWARDED: '. $forward);

  // Body content

  echo "<html>
  <head>
  <title>Show IP</title>
  <meta name='description' content='A simple page to find out your IP address and if you are behind any proxies. The page is designed to be accessed via a text-based browser such as Lynx or via a header check with a program such as curl.'>
  </head>
  <body>
  <p>This page is designed to be accessed with a text-based browser such as Lynx.</p>
  <p>== Your IP address ==</p>
  <p>$ip</p>
  <p>== Proxies ==</p>
  <p>HTTP_X_FORWARDED: $forwarded</p> 
  <p>HTTP_X_FORWARDED_FOR: $forwarded_for</p>
  <p>HTTP_FORWARDED: $forwarded2</p>
  <p>FORWARDED: $forward</p>
  </body> 
  </html>";
}
?>