#!/usr/bin/env python3


import sys
import sympy


def factorize(n):
    factors = sympy.factorint(n)
    if len(factors) != 2:
        return None
    else:
        return factors

def main(filename):
    with open(filename, 'r') as file:
        for line in file:
            n = int(line)
            factor_pairs = factorize(n)
            if factor_pairs:
                p, q = factor_pairs.keys()
                print(f"{n}={p}*{q}")
            else:
                print(f"Unable to factorize {n}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)
    filename = sys.argv[1]
    main(filename)
