<?php

class day1 {
  public function part1() {
    $total = 0;
    $freqs = $this->read_input("./day1/input.txt");
    
    foreach ($freqs as $freq) {
      $total += $freq;
    }

    echo $total . "\n";
  }

  public function part2() {
    $hits = array();
    $total = 0;
    $freqs = $this->read_input("./day1/input.txt");

    for ($x = 0; $x < count($freqs); $x++) {
      $total += $freqs[$x];
      if (in_array($total, $hits)) {
        echo $total;
        exit();
      }

      array_push($hits, $total);
      if (($x + 1) == count($freqs)) {
        $x = -1;
      }
    }
  }

  private function read_input($file) {
    return explode("\n", file_get_contents($file));
  }
}

?>