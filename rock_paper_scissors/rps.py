#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    combinations = [["rock"], ["paper"], ["scissors"]]
    original_n = n

    def inner_rps(n):
        if n == 1:
            new_list = [x for x in combinations if len(x) == original_n]
            return new_list
        else:
            for i in range(len(combinations)):
                combinations.append(combinations[i] + ["rock"])
                combinations.append(combinations[i] + ["paper"])
                combinations.append(combinations[i] + ["scisors"])
            return inner_rps(n - 1)
    return inner_rps(n)


if __name__ == "__main__":
    # Test out your implementation from the command line
    # with `python rps.py [n]` with different n values
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
