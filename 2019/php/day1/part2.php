<?php

include "helper.php";

$file = fopen("input.txt", "r");
$total_fuel = 0;

while(!feof($file)) {
  $mass = fgets($file);
  $module_fuel = calculate_fuel(intval($mass));

  while($module_fuel > 0) {
    $total_fuel += $module_fuel;
    $module_fuel = calculate_fuel($module_fuel);
  }
}

echo $total_fuel;

?>