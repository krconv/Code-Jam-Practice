from __future__ import print_function
import math
import sys
from queue import Queue


def debug(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

"""
The solution to the problem.
"""
def solution(pancakes, flipper_size):
    trials = {}
    queue = Queue()

    trials[pancakes] = 0
    queue.put(pancakes)

    while (not queue.empty()):
        current = queue.get()
        if (is_done(current)):
            return trials[current]
        for pos in range(len(pancakes) - flipper_size + 1):
            if (should_flip(current, flipper_size, pos)):
                flipped = flip(current, flipper_size, pos)
                if (flipped not in trials):
                    trials[flipped] = trials[current] + 1
                    queue.put(flipped)
    return -1

def should_flip(pancakes, flipper_size, position):
    for i in range(position, position + flipper_size):
        if (pancakes[i] == '-'):
            return True
    return False

def flip(pancakes, flipper_size, position):
    result = list(pancakes)
    for i in range(position, position + flipper_size):
        result[i] = '+' if result[i] == '-' else '-'
    return ''.join(result)

def is_done(pancakes):
    return not '-' in pancakes

"""
Run the algorithm using input from standard input.
"""
def main():
    test_count = int(input())
    for i in range(1, test_count + 1):
        test = input().split(' ')
        pancakes = test[0]
        flipper_size = int(test[1])
        result = solution(pancakes, flipper_size)
        print(f"Case #{i}: {result if result != -1 else 'IMPOSSIBLE'}")

if __name__ == "__main__":
    main()
