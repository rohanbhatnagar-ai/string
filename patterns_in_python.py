"""
=====================================================
        PATTERNS IN PYTHON - WITH CODE
                @pycode.hubb
=====================================================
A collection of 14 classic console patterns.
Run this file to print all patterns one after another,
or call any individual function (e.g. pattern_5_diamond()).
"""


# 1. Right Triangle
def pattern_1_right_triangle():
    for i in range(1, 6):
        print("* " * i)


# 2. Inverted Triangle
def pattern_2_inverted_triangle():
    for i in range(5, 0, -1):
        print("* " * i)


# 3. Pyramid
def pattern_3_pyramid():
    n = 5
    for i in range(1, n + 1):
        print("  " * (n - i) + "* " * i)


# 4. Inverted Pyramid
def pattern_4_inverted_pyramid():
    n = 5
    for i in range(n, 0, -1):
        print("  " * (n - i) + "* " * i)


# 5. Diamond
def pattern_5_diamond():
    n = 5
    for i in range(1, n + 1):
        print("  " * (n - i) + "* " * i)
    for i in range(n - 1, 0, -1):
        print("  " * (n - i) + "* " * i)


# 6. Number Triangle
def pattern_6_number_triangle():
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


# 7. Same Number Triangle
def pattern_7_same_number_triangle():
    for i in range(1, 6):
        print((str(i) + " ") * i)


# 8. Alphabet Triangle
def pattern_8_alphabet_triangle():
    for i in range(65, 70):
        for j in range(65, i + 1):
            print(chr(j), end=" ")
        print()


# 9. Floyd's Triangle
def pattern_9_floyds_triangle():
    n = 1
    for i in range(1, 6):
        for j in range(i):
            print(n, end=" ")
            n += 1
        print()


# 10. Pascal's Triangle
def pattern_10_pascals_triangle():
    from math import comb
    n = 6
    for i in range(n):
        print("  " * (n - i), end="")
        for j in range(i + 1):
            print(comb(i, j), end=" ")
        print()


# 11. Hollow Square
def pattern_11_hollow_square():
    n = 5
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


# 12. Hollow Triangle
def pattern_12_hollow_triangle():
    n = 5
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if j == 1 or j == i or i == n:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


# 13. Reversed Alphabet Triangle
def pattern_13_reversed_alphabet_triangle():
    for i in range(69, 64, -1):
        for j in range(69, i - 1, -1):
            print(chr(j), end=" ")
        print()


# 14. Checkerboard
def pattern_14_checkerboard():
    n = 6
    for i in range(n):
        for j in range(n):
            print("\u25a0" if (i + j) % 2 == 0 else "\u25a1", end=" ")
        print()


# ----------------------------------------------------
# Run every pattern in order
# ----------------------------------------------------
PATTERNS = [
    ("1. Right Triangle", pattern_1_right_triangle),
    ("2. Inverted Triangle", pattern_2_inverted_triangle),
    ("3. Pyramid", pattern_3_pyramid),
    ("4. Inverted Pyramid", pattern_4_inverted_pyramid),
    ("5. Diamond", pattern_5_diamond),
    ("6. Number Triangle", pattern_6_number_triangle),
    ("7. Same Number Triangle", pattern_7_same_number_triangle),
    ("8. Alphabet Triangle", pattern_8_alphabet_triangle),
    ("9. Floyd's Triangle", pattern_9_floyds_triangle),
    ("10. Pascal's Triangle", pattern_10_pascals_triangle),
    ("11. Hollow Square", pattern_11_hollow_square),
    ("12. Hollow Triangle", pattern_12_hollow_triangle),
    ("13. Reversed Alphabet Triangle", pattern_13_reversed_alphabet_triangle),
    ("14. Checkerboard", pattern_14_checkerboard),
]


def main():
    for title, func in PATTERNS:
        print(f"\n{title}")
        print("-" * len(title))
        func()


if __name__ == "__main__":
    main()
