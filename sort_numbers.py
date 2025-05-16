#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python sort_numbers.py <num1> <num2> ... <numN>")
        sys.exit(1)
    try:
        numbers = [float(arg) for arg in sys.argv[1:]]
    except ValueError:
        print("All arguments must be numbers.")
        sys.exit(1)
    sorted_numbers = sorted(numbers)
    print("Sorted numbers:", sorted_numbers) 