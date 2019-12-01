<?php

include "helper.php";

$file = fopen("input.txt", "r");
$fuel = 0;

while(!feof($file)) {
  $mass = fgets($file);
  $fuel += calculate_fuel(intval($mass));
}

echo $fuel;

?>