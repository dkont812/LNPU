import sys
def find_pairs():
    for arg in sys.argv:
        numbers = list(map(int, sys.argv[1:]))

    pairs = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            pairs.append((numbers[i], numbers[j]))

    for a,b in pairs:
        if a + b == 10:
            print(f"({a}+{b})")
