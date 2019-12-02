extern crate clap;
mod day1;
use clap::{App, SubCommand};

fn main() {
  let matches = App::new("Advent of Code")
    .version("2019")
    .author("Matthew Salazar <m@tthewsalazar.com>")
    .subcommand(SubCommand::with_name("day1"))
    .get_matches();

  match matches.subcommand_name() {
    Some("day1") => {
      day1::part1();
      day1::part2();
    }
    None => println!("Day not found!"),
    _ => println!("Day not found!"),
  }
}
