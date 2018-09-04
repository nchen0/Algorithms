#!/usr/bin/python

import sys
import itertools


def climbing_stairs(n):
    if n == 0:
        return 1
    original_list = []

# Find ALL combinations of 1,2,3 possible, with repeats, of n times and add it to original_list.
    for i in range(1, n+1):
        original_list.append(list(itertools.product('123', repeat=i)))

# Extract each nested list, and put them as integers.
    extracted_list = []
    for nested_list in original_list:
        for inner_list in nested_list:
            extracted_list.append((list(map(int, inner_list))))

# Return any list combination that adds up to n.
    return len([sum(j) for j in extracted_list if sum(j) == n])


print(climbing_stairs(15))

if __name__ == "__main__":
    # Test out your implementation from the command line
    # with `python climbing_stairs.py [n]` with different n values
    if len(sys.argv) > 1:
        num_stairs = int(sys.argv[1])
        print("There are {ways} ways for a child to jump {n} stairs.".format(
            ways=climbing_stairs(num_stairs), n=num_stairs))
    else:
        print('Usage: climbing_stairs.py [num_stairs]')
