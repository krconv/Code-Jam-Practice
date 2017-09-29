from __future__ import print_function
import math
import sys
from queue import Queue


def debug(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

"""
The solution to the problem.
"""
def solution(N):
    digits = [int(x) for x in str(N)]
    if (is_tidy(N)):
        return N
    pos = 0
    while (digits[pos] <= digits[pos + 1]):
        pos += 1
    while (pos > 0 and digits[pos] == digits[pos - 1]):
        pos -= 1
    digits[pos] -= 1
    for i in range(pos + 1, len(digits)):
        digits[i] = 9
    return int(''.join(map(str, digits)))

def is_tidy(number):
    digits = [int(x) for x in str(number)]
    for i in range(len(digits) - 1):
        if (digits[i + 1] < digits[i]):
            return False
    return True

"""
Run the algorithm using input from standard input.
"""
def main():
    test_count = int(input())
    for i in range(1, test_count + 1):
        N = int(input())
        result = solution(N)
        print(f"Case #{i}: {result}")

if __name__ == "__main__":
    main()
