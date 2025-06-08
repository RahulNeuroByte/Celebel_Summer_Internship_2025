# To implement pyramid of *

n = int(input("Enter number of rows for Pyramid Pattern: "))
print("\nPyramid Pattern:")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
