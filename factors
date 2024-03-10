#!/usr/bin/env python3


import sys


def factorize(n):
    factors = []
    for i in range(2, n//2 + 1):
        if n % i == 0:
            factors.append((i, n//i))
    return factors


def main(filename):
    with open(filename, 'r') as file:
        for line in file:
            n = int(line)
            factor_pairs = factorize(n)
            for pair in factor_pairs:
                print(f"{n}={pair[0]}*{pair[1]}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)
    filename = sys.argv[1]
    main(filename)
