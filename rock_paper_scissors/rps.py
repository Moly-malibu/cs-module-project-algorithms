#!/usr/bin/python
import sys
  
def make(options, arr, number_plays, possible_plays): 
  if number_plays == 0: 
    possible_plays.append(arr)
    return

  for index in range(len(options)):
    arr_options = arr.copy()
    arr_options.append(options[index])
    
    make(options, arr_options, number_plays - 1, possible_plays)

def rock_paper_scissors(num_plays):
  options = ["rock", "paper", "scissors"]  
  possible_plays = []

  make(options, [], num_plays, possible_plays) 

  return possible_plays 

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')