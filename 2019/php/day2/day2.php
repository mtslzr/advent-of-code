<?php

class day2 {
  public function part1() {
    $nums = $this->run_intcode($this->read_input("./day2/input.txt"));
    echo $nums[0];
  }

  public function part2() {
  }

  private function read_input($file) {
    return explode(",", file_get_contents($file));
  }

  private function run_intcode($nums, $noun = 12, $verb = 2) {
    $x = 0;
    $nums[1] = $noun;
    $nums[2] = $verb;

    while($x < count($nums)) {
      if($nums[$x] == 99) {
        break;
      }

      $a = $nums[$x+1];
      $b = $nums[$x+2];
      $c = $nums[$x+3];

      if($nums[$x] == 1) {
        $nums[$c] = $nums[$a] + $nums[$b];
      } else if($nums[$x] == 2) {
        $nums[$c] = $nums[$a] * $nums[$b];
      } else {
        echo "Unexpected optcode: " . $num[$x];
      }
      $x += 4;
    }

    return $nums;
  }
}

?>