#!/usr/bin/env python3
"""
bitwise_matching.py:
Given an integer n, returns the next higher integer with the same number of binary 1s.
Uses classic bit manipulation techniques.
"""

def next_higher_same_bits(n):
    """
    Computes the next higher integer with the same number of 1s in its binary representation.

    Parameters:
      n: An integer.

    Returns:
      The next integer with the same count of binary 1s, or -1 if no such number exists.
    """
    c = n
    c0 = 0  # Count of trailing zeros.
    c1 = 0  # Count of ones immediately following the trailing zeros.

    # Count trailing zeros.
    while (c & 1) == 0 and c:
        c0 += 1
        c //= 2

    # Count the ones.
    while c & 1:
        c1 += 1
        c //= 2

    # If there is no valid position to flip.
    if c0 + c1 == 31 or c0 + c1 == 0:
        return -1

    p = c0 + c1  # Position of rightmost non-trailing zero.
    # Flip the rightmost non-trailing zero.
    n |= (1 << p)
    # Clear bits to the right of p.
    n &= ~((1 << p) - 1)
    # Insert (c1-1) ones on the right.
    n |= (1 << (c1 - 1)) - 1
    return n



test_values = [6, 92]  # Example: for 6 (binary 110) next should be 9 (binary 1001)
for n in test_values:
    result = next_higher_same_bits(n)
    print(f"Next higher for {n}: {result}")
