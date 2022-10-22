"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in range(len(items)):
        frequencies[str(items[i])] = 0

    for j in range(len(items)):
        frequencies[str(items[j])] += 1

    return frequencies
