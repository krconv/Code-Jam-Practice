from __future__ import print_function
import math
import sys
from queue import Queue


def debug(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


"""
The solution to the problem.
"""
def solution(cake):
    checked = {}
    claims = {}
    for row in range(len(cake)):
        for col in range(len(cake[0])):
            if (has_initial(cake[row][col])):
                initial = cake[row][col]
                if (initial not in claims):
                    claims[initial] = []
                    checked[initial] = []
                claims[initial].append((row, col))
                checked[initial].append((row, col))
                for direction in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    if (not in_cake(cake, row + direction[0], col + direction[1])):
                        continue
                    if (can_expand(cake, initial, claims[initial], row, col, direction)):
                        adds = expand(cake, initial, claims[initial], row, col, direction)
                        while (len(adds) != 0):
                            add = adds[0]
                            adds.remove(add)
                            if (can_expand(cake, initial, claims[initial], add[0], add[1], direction)):
                                adds += expand(cake, initial, claims[initial], add[0], add[1], direction)

    return cake

def has_initial(square):
    return square != '?'

def in_cake(cake, row, col):
    return row >= 0 and row < len(cake) and col >= 0 and col < len(cake[0])

def can_expand(cake, initial, claims, row, col, direction):
    expanding = 0 if direction[1] == 0 else 1
    start = (row, col)[expanding]
    for claim in claims:
        if (claim[expanding] == start):
            if (not in_cake(cake,claim[0] + direction[0], claim[1] + direction[1]) or has_initial(cake[claim[0] + direction[0]][claim[1] + direction[1]])):
                return False
    return True

def expand(cake, initial, claims, row, col, direction):
    adds = []
    expanding = 0 if direction[1] == 0 else 1
    start = (row, col)[expanding]
    for claim in claims:
        if (claim[expanding] == start):
            cake[claim[0] + direction[0]][claim[1] + direction[1]] = initial
            adds.append((claim[0] + direction[0], claim[1] + direction[1]))
    claims += adds
    return adds

"""
Run the algorithm using input from standard input.
"""
def main():
    test_count = int(input())
    for i in range(1, test_count + 1):
        rows = int(input().split()[0])
        cake = []
        for row in range(rows):
            cake.append(list(input()))
        result = solution(cake)
        print(f"Case #{i}:")
        for row in range(len(result)):
            print(''.join(cake[row]))


if __name__ == "__main__":
    main()
