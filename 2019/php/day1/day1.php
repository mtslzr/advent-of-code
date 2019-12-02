<?php

class day1 {
  public function part1() {
    $file = fopen("./day1/input.txt", "r");
    $fuel = 0;

    while(!feof($file)) {
      $mass = fgets($file);
      $fuel += $this->calculate_fuel(intval($mass));
    }

    echo $fuel . "\n";
  }

  public function part2() {
    $file = fopen("./day1/input.txt", "r");
    $total_fuel = 0;

    while(!feof($file)) {
      $mass = fgets($file);
      $module_fuel = $this->calculate_fuel(intval($mass));

      while($module_fuel > 0) {
        $total_fuel += $module_fuel;
        $module_fuel = $this->calculate_fuel($module_fuel);
      }
    }

    echo $total_fuel . "\n";
  }

  private function calculate_fuel($mass) {
    return floor($mass / 3) - 2;
  }
}

?>