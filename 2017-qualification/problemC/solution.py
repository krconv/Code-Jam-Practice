from __future__ import print_function
import math
import sys
from queue import Queue


def debug(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

"""
The solution to the problem.
"""
def solution(stalls, number):
    if (number == 1):
        return [stalls // 2, (stalls - 1) // 2]
    first = int(math.pow(2, int(math.log(number, 2))))
    middle = first + int(first // 2)

    if (number % 2 == 0):
        if (number < middle):
            parent = number // 2
        else:
            parent = (first + (number - middle)) // 2
    else:
        if (number < middle):
            parent = (middle + (middle - number)) // 2
        else:
            parent = number // 2
    gap = solution(stalls, int(parent))[0 if number < middle else 1]
    return find_stalls_adjacent(gap)

def find_stalls_adjacent(gap):
    picked = (gap + 1) // 2
    debug(f"Gap: {gap} Picked: {picked} Left: {picked - 1} Right: {gap - picked}")
    return [picked - 1, gap - picked]

"""
Run the algorithm using input from standard input.
"""
def main():
    test_count = int(input())
    for i in range(1, test_count + 1):
        args = input().split(' ')
        stalls = int(args[0])
        number = int(args[1])
        result = solution(stalls, number)
        print(f"Case #{i}: {max(result)} {min(result)}")

if __name__ == "__main__":
    main()